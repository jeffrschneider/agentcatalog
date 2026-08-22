#!/usr/bin/env python3
"""Build one Agent Plugin package per abstract agent.

Reads every document in agents/ and every reference process in
processes/, then writes plugins/<slug>/ for each abstract agent: a
plugin.json manifest, a README, one skill per capability the abstract
agent has, and the obligations sidecar under
com.agentcatalog.agent/.

Which activities each capability covers is read from skills/<slug>.md,
because the activity names cannot make that grouping on their own.

The build is a pure function of the source documents. Running it twice
produces byte-identical output, so it is safe to run on every change.

Usage: python tools/build-plugins.py
"""

import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
AGENTS_DIR = os.path.join(ROOT, "agents")
PROCESSES_DIR = os.path.join(ROOT, "processes")
PLUGINS_DIR = os.path.join(ROOT, "plugins")
# Which activities each capability covers. Written by hand, because grouping
# activities into capabilities is a judgement call the names cannot make.
SKILLS_DIR = os.path.join(ROOT, "skills")

NAMESPACE = "com.agentcatalog.agent"
SCHEMA = "https://agent-plugins.org/schemas/1.1.0/plugin.schema.json"
SITE = "https://agentcatalog.com"
REPOSITORY = "https://github.com/jeffrschneider/agentcatalog"
LICENSE = "CC-BY-4.0"
WIDTH = 72

# The agent documents were written with "## Seats" and are being renamed
# to "## Processes". Both spellings parse.
PROCESS_HEADINGS = ("Processes", "Seats")


# --------------------------------------------------------------------
# small text helpers
# --------------------------------------------------------------------

def slugify(text):
    """Kebab-case slug, used for skill directories and server roles."""
    text = text.lower().replace("&", " and ")
    text = re.sub(r"['‘’]", "", text)
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def flatten(text):
    """Collapse a wrapped paragraph onto one line."""
    return " ".join(text.split())


def sentences(paragraph):
    """Split a paragraph into sentences."""
    paragraph = flatten(paragraph)
    if not paragraph:
        return []
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", paragraph) if s]


def sentence_case(text):
    """Capitalize the first letter and end with a full stop."""
    text = flatten(text)
    if not text:
        return text
    text = text[0].upper() + text[1:]
    if text[-1] not in ".!?":
        text += "."
    return text


NUMBER_WORDS = [
    "no", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
]

# A space inside a markdown link would let the wrapper break the link in
# half, so links are glued together with this and split apart afterwards.
GLUE = "\x00"


def number_word(count):
    """Spell out a small number, so a sentence never opens with a digit."""
    if count < len(NUMBER_WORDS):
        return NUMBER_WORDS[count]
    return str(count)


def wrap(text, width=WIDTH, first="", cont=""):
    """Wrap to `width` columns without ever breaking a word."""
    lines, line, empty = [], first, True
    for word in flatten(text).split(" "):
        if empty:
            line, empty = line + word, False
        elif len(line) + 1 + len(word) <= width:
            line = line + " " + word
        else:
            lines.append(line)
            line = cont + word
    lines.append(line)
    return "\n".join(lines).replace(GLUE, " ")


def yaml_scalar(text):
    """Render a string as a YAML scalar, quoting only when it has to."""
    unsafe = (
        not text
        or text != text.strip()
        or text[0] in "-?:,[]{}#&*!|>'\"%@`"
        or ": " in text
        or " #" in text
        or text.endswith(":")
    )
    if unsafe:
        return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return text


def write(path, text):
    """Write UTF-8 with Unix newlines, creating parent directories."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


# --------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------

def sections(text):
    """Map every `## Heading` in a document to its body."""
    found = {}
    for match in re.finditer(r"^## ([^\n]+)\n(.*?)(?=\n## |\Z)", text, re.S | re.M):
        found[match.group(1).strip()] = match.group(2).strip()
    return found


def section(found, *names):
    for name in names:
        if name in found:
            return found[name]
    return ""


def bullets(body):
    """Bullet items from a section body, with wrapped lines joined.

    Anything after the bullets is returned separately, because several
    Grants sections end with a sentence about what was left out.
    """
    items, note = [], []
    for line in body.split("\n"):
        if items and not line.strip():
            note.append(line)
        elif note:
            note.append(line)
        elif line.startswith("- "):
            items.append(line[2:].strip())
        elif line.startswith("  ") and items:
            items[-1] += " " + line.strip()
        elif line.strip():
            note.append(line)
    return items, flatten("\n".join(note))


def read_process(path):
    """One reference process: its id, its title, and its activities."""
    text = open(path, encoding="utf-8").read()
    process_id = re.search(r"^`(ref/\S+) v(\d+)`", text, re.M)
    title = re.search(r"^# (.*)$", text, re.M).group(1).strip()
    if title.startswith("Reference process:"):
        title = title[len("Reference process:"):].strip()
    activities = {}
    row = r"^\| *(\d+) *\| *(.*?) *\| *(.*?) *\| *(.*?) *\|\s*$"
    for match in re.finditer(row, text, re.M):
        activities[match.group(2)] = {
            "number": int(match.group(1)),
            "happens": match.group(3),
        }
    return {
        "id": process_id.group(1),
        "version": int(process_id.group(2)),
        "title": title,
        "activities": activities,
        "department": os.path.basename(os.path.dirname(path)),
        "path": os.path.relpath(path, ROOT).replace(os.sep, "/"),
    }


def split_activities(names, known):
    """Split a comma-separated activity list.

    Two activity names in the catalog contain a comma of their own, so
    a plain split would tear them in half. Take the longest run of
    comma-separated pieces that matches an activity the process really
    has, and fall back to the single piece when nothing matches.
    """
    pieces = [p.strip() for p in names.split(",")]
    out, i = [], 0
    while i < len(pieces):
        for j in range(len(pieces), i, -1):
            candidate = ", ".join(pieces[i:j])
            if candidate in known:
                out.append(candidate)
                i = j
                break
        else:
            out.append(pieces[i])
            i += 1
    return out


def read_agent(path, processes):
    """One abstract agent document, parsed into the fields a plugin needs."""
    text = open(path, encoding="utf-8").read()
    found = sections(text)
    header = re.search(r"^`(\S+) v(\d+)`", text, re.M)
    slug, version = header.group(1), int(header.group(2))
    purpose = re.search(r"^\*\*purpose:\*\*(.*?)(?=\n## |\Z)", text, re.S | re.M)

    problems = []

    held = []
    lines, _ = bullets(section(found, *PROCESS_HEADINGS))
    for line in lines:
        match = re.match(r"^`([^`]+)`\s*/\s*(.*)$", line)
        if not match:
            problems.append("could not read the process line: " + line)
            continue
        process_id, names = match.group(1), match.group(2)
        process = processes.get(process_id)
        if process is None:
            problems.append("names a process that does not exist: " + process_id)
            continue
        activities = split_activities(names, process["activities"])
        for name in activities:
            if name not in process["activities"]:
                problems.append(
                    "names an activity %s does not have: %s" % (process_id, name)
                )
        held.append({"process": process_id, "activities": activities})

    servers = []
    grants, grants_note = bullets(section(found, "Grants"))
    for grant in grants:
        match = re.match(r"^(.*?)\s*\(([^()]*)\)\s*(?:-\s*(.*))?$", grant)
        if not match:
            problems.append("could not read the grant line: " + grant)
            continue
        entry = {
            "name": match.group(1).strip(),
            "role": slugify(re.sub(r"^(the|a|an) ", "", match.group(1).strip())),
            "access": match.group(2).strip(),
        }
        if match.group(3):
            entry["needs"] = sentence_case(match.group(3))
        servers.append(entry)

    escalates, _ = bullets(section(found, "Escalates"))

    return {
        "slug": slug,
        "version": version,
        "title": re.search(r"^# (.*)$", text, re.M).group(1).strip(),
        "purpose": flatten(purpose.group(1)) if purpose else "",
        "held": held,
        "works": flatten(section(found, "Patterns")),
        "servers": servers,
        "servers_note": grants_note,
        "records": flatten(section(found, "Records")),
        "escalates": [flatten(e) for e in escalates],
        "not": flatten(section(found, "Not")),
        "problems": problems,
        "path": os.path.relpath(path, ROOT).replace(os.sep, "/"),
    }


# --------------------------------------------------------------------
# deriving the manifest
# --------------------------------------------------------------------

def describe(agent):
    """One or two sentences of purpose, behind the agent's name."""
    said = sentences(agent["purpose"])
    kept = said[:1]
    if len(said) > 1 and len(kept[0]) < 120 and len(kept[0]) + len(said[1]) <= 300:
        kept.append(said[1])
    return "The %s abstract agent. %s" % (agent["slug"], " ".join(kept))


def keywords(agent, processes):
    """Search terms: what it is, where it lives, and its busiest processes."""
    busiest = sorted(
        agent["held"], key=lambda h: (-len(h["activities"]), h["process"])
    )[:3]
    words = ["abstract-agent", "reference", department(agent, processes)]
    words += [h["process"].rsplit("/", 1)[-1] for h in busiest]
    words.append("abstract")
    return words


def department(agent, processes):
    """The department the abstract agent works in."""
    counts = {}
    for held in agent["held"]:
        name = processes[held["process"]]["department"]
        counts[name] = counts.get(name, 0) + 1
    if not counts:
        return "marketing"
    return sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[0][0]


def manifest(agent, processes):
    return {
        "$schema": SCHEMA,
        "name": agent["slug"],
        "version": "%d.0.0" % agent["version"],
        "description": describe(agent),
        "author": {"name": "AgentCatalog", "url": SITE},
        "homepage": "%s/abstract-agents/%s" % (SITE, agent["slug"]),
        "repository": REPOSITORY,
        "license": LICENSE,
        "keywords": keywords(agent, processes),
        "extensions": {
            NAMESPACE: {
                "agent": agent["slug"],
                "agentVersion": agent["version"],
                "department": department(agent, processes),
                "abstract": True,
                "works": agent["works"],
                "servers": agent["servers"],
                "records": sentences(agent["records"]),
                "escalates": agent["escalates"],
                "not": sentences(agent["not"]),
                "processes": agent["held"],
            }
        },
    }


def read_skill_map(path, slug):
    """The capabilities an abstract agent has, and the activities each covers.

    A skill is one thing the agent knows how to do. Activities are named per
    process, so the same capability turns up under many names: watching the
    first weeks of a launch and watching the registrations for a webinar are
    the same work on a different subject. Grouping them is a judgement call,
    so it is written down in skills/<agent>.md and read here rather than
    guessed from the activity names.
    """
    text = open(path, encoding="utf-8").read()
    first = text.strip().split("\n")[0]
    head = re.match(r"^#\s+([a-z0-9-]+)\s*$", first)
    if not head or head.group(1) != slug:
        raise SystemExit("%s must start with '# %s'" % (path, slug))

    caps = []
    for block in re.split(r"^##\s+", text, flags=re.M)[1:]:
        lines = block.split("\n")
        cap_slug = lines[0].strip()
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", cap_slug):
            raise SystemExit("%s: '%s' is not a capability slug" % (path, cap_slug))
        body = "\n".join(lines[1:])
        prose, marker, covered = body.partition("covers:")
        if not marker:
            raise SystemExit("%s: capability '%s' has no covers: list" % (path, cap_slug))
        names = [
            line.strip()[2:].strip()
            for line in covered.split("\n")
            if line.strip().startswith("- ")
        ]
        if not names:
            raise SystemExit("%s: capability '%s' covers nothing" % (path, cap_slug))
        caps.append(
            {"slug": cap_slug, "description": flatten(prose).strip(), "covers": names}
        )
    if not caps:
        raise SystemExit("%s names no capabilities" % path)
    return caps


def collect_skills(agent, processes, skills_dir):
    """One skill per capability, carrying every activity it covers."""
    path = os.path.join(skills_dir, agent["slug"] + ".md")
    if not os.path.exists(path):
        raise SystemExit(
            "no skill map for %s. Every abstract agent needs skills/%s.md "
            "saying which activities each capability covers."
            % (agent["slug"], agent["slug"])
        )
    caps = read_skill_map(path, agent["slug"])

    uses_of = {}
    for held in agent["held"]:
        process = processes[held["process"]]
        for name in held["activities"]:
            activity = process["activities"].get(name)
            if activity is None:
                continue
            uses_of.setdefault(name, []).append(
                {
                    "process": process["id"],
                    "title": process["title"],
                    "path": process["path"],
                    "number": activity["number"],
                    "happens": activity["happens"],
                }
            )

    claimed = {}
    skills = []
    for cap in caps:
        activities = []
        for name in cap["covers"]:
            if name not in uses_of:
                raise SystemExit(
                    "%s claims '%s', which %s does not hold"
                    % (path, name, agent["slug"])
                )
            if name in claimed:
                raise SystemExit(
                    "%s: '%s' is covered by both '%s' and '%s'"
                    % (path, name, claimed[name], cap["slug"])
                )
            claimed[name] = cap["slug"]
            activities.append(
                {
                    "name": name,
                    "uses": sorted(uses_of[name], key=lambda use: use["process"]),
                }
            )
        skills.append(
            {
                "slug": cap["slug"],
                "title": cap["slug"].replace("-", " ").capitalize(),
                "description": cap["description"],
                "activities": sorted(activities, key=lambda a: a["name"]),
            }
        )

    missing = sorted(set(uses_of) - set(claimed))
    if missing:
        raise SystemExit(
            "%s leaves %d of %s's activities uncovered, starting with '%s'"
            % (path, len(missing), agent["slug"], missing[0])
        )
    return sorted(skills, key=lambda skill: skill["slug"])


# --------------------------------------------------------------------
# writing the package
# --------------------------------------------------------------------

def skill_page(agent, skill):
    """One capability, and every activity where the agent exercises it."""
    procs = []
    for activity in skill["activities"]:
        for use in activity["uses"]:
            if use["process"] not in procs:
                procs.append(use["process"])
    procs.sort()

    if len(procs) == 1:
        where = "Use it when running `%s`." % procs[0]
    elif len(procs) <= 3:
        where = "Use it when running %s and `%s`." % (
            ", ".join("`%s`" % p for p in procs[:-1]),
            procs[-1],
        )
    else:
        where = "Use it when running `%s` and %d other reference processes." % (
            procs[0],
            len(procs) - 1,
        )

    summary = sentences(skill["description"])[0] if skill["description"] else skill["title"]

    out = [
        "---",
        "name: " + skill["slug"],
        "description: " + yaml_scalar(summary + " " + where),
        "license: " + LICENSE,
        "metadata:",
        "  agent: " + agent["slug"],
        '  agent-version: "%d"' % agent["version"],
        "---",
        "",
        "# " + skill["title"],
        "",
        "## What it does",
        "",
        wrap(skill["description"]),
        "",
        "## Where it happens",
        "",
        wrap(
            "The agent does this in %s across %s. Each one names the activity "
            "as that process words it."
            % (
                "one activity" if len(skill["activities"]) == 1
                else "%s activities" % number_word(len(skill["activities"])),
                "one reference process" if len(procs) == 1
                else "%s reference processes" % number_word(len(procs)),
            )
        ),
        "",
    ]

    for activity in skill["activities"]:
        out.append("- **%s**" % activity["name"])
        for use in activity["uses"]:
            link = "[%s](%s%s)" % (use["title"], "../" * 4, use["path"])
            out.append(
                wrap(
                    "`%s`, activity %d - %s"
                    % (use["process"], use["number"], link.replace(" ", GLUE)),
                    first="  - ",
                    cont="    ",
                )
            )

    out += [
        "",
        "## What to record",
        "",
        wrap(agent["records"]),
        "",
        wrap(
            "That contract covers every activity this abstract agent takes on, "
            "and it is repeated in `%s/RECORDS.md`. What the abstract agent "
            "does not do is in `%s/NOT.md`." % (NAMESPACE, NAMESPACE)
        ),
        "",
    ]
    return "\n".join(out)


def readme_page(agent, skills):
    held = agent["held"]
    shown = [h["process"] for h in held[:6]]
    listing = ", ".join("`%s`" % p for p in shown)
    if len(held) > len(shown):
        listing += ", and %d more" % (len(held) - len(shown))

    skill_count = (
        "one skill" if len(skills) == 1
        else "%s skills" % number_word(len(skills))
    )
    return "\n".join(
        [
            "# " + agent["slug"],
            "",
            wrap(
                "This is an abstract agent, published as an Agent Plugin. An "
                "abstract agent is a job description rather than an "
                "implementation. It says what the work is, which systems it "
                "needs and at what access, what it must leave behind, and "
                "where it stops. Any agent that leaves the records can "
                "implement it."
            ),
            "",
            wrap(
                "The plugin carries %s, no `mcp.json`, and everything the "
                "abstract agent owes under `%s/`." % (skill_count, NAMESPACE)
            ),
            "",
            "## Why there is no mcp.json",
            "",
            wrap(
                "A conformant server entry in `mcp.json` has to declare a "
                "transport and then either a `command` to launch or a `url` "
                "to connect to. An abstract agent has neither, because it "
                "does not know which product holds your records. Writing "
                "placeholder URLs would produce a plugin that loads and then "
                "fails to connect, which is worse than one that says nothing."
            ),
            "",
            wrap(
                "Section 6.2 makes a missing component location not an error, "
                "so the file is absent and the systems this abstract agent "
                "needs are declared instead under "
                '`extensions["%s"].servers`, as a role, an access level and '
                "what the access is for. Whoever builds an agent from this "
                "plugin writes the `mcp.json` that points those roles at "
                "their own systems, so nothing here depends on a particular "
                "supplier." % NAMESPACE
            ),
            "",
            "## Why the obligations are in an extension",
            "",
            wrap(
                "The specification defines two component types, skills and "
                "MCP servers, and both describe what a plugin can do. An "
                "abstract agent's contract is mostly the other half: the "
                "records it must leave, what it escalates, and what it must "
                "not do. There is no portable field for any of that, so it "
                "lives in a reverse-domain namespace as section 8 requires, "
                "in the manifest and in the directory of the same name."
            ),
            "",
            "## Where this abstract agent is used",
            "",
            wrap(
                listing
                + ". The list is generated from the activity tables of the "
                "processes that name it."
            ),
            "",
            "%s/abstract-agents/%s" % (SITE, agent["slug"]),
            "",
        ]
    )


def records_page(agent):
    return "\n".join(
        [
            "# The records this abstract agent must leave",
            "",
            wrap(
                "This is the contract. An agent implementing `%s` leaves the "
                "following behind, on every run." % agent["slug"]
            ),
            "",
            wrap(agent["records"]),
            "",
            wrap(
                "An agent that leaves less than this does not implement `%s`, "
                "whatever else it does well." % agent["slug"]
            ),
            "",
        ]
    )


def servers_page(agent):
    servers = agent["servers"]
    detailed = any("needs" in server for server in servers)
    count = "One system" if len(servers) == 1 else (
        number_word(len(servers)).capitalize() + " systems"
    )

    out = [
        "# The systems this abstract agent needs",
        "",
        wrap(
            "%s, named by role rather than by product. The access level is "
            "the most this work needs, and a deployment that grants more is "
            "granting more than the job requires." % count
        ),
        "",
    ]
    if detailed:
        out += ["| Role | Access | What the access is for |", "|---|---|---|"]
        for server in servers:
            cells = [server["name"], server["access"], server.get("needs", "")]
            out.append("|" + "|".join(" %s " % c.strip() for c in cells) + "|")
    else:
        out += ["| Role | Access |", "|---|---|"]
        for server in servers:
            out.append("| %s | %s |" % (server["name"], server["access"]))
    out.append("")
    if agent["servers_note"]:
        out += [wrap(agent["servers_note"]), ""]
    out += [
        wrap(
            "Whoever builds an agent from this plugin writes the `mcp.json` "
            "that points these roles at their own systems. Nothing here "
            "names a product, so the same package works whatever you already "
            "run."
        ),
        "",
    ]
    return "\n".join(out)


def not_page(agent):
    out = ["# Where this abstract agent stops", "", wrap(agent["not"]), ""]
    if agent["escalates"]:
        out += ["## What always goes to a person", ""]
        for item in agent["escalates"]:
            out.append(wrap(item, first="- ", cont="  "))
        out.append("")
    return "\n".join(out)


def build(agent, processes, skills_dir):
    skills = collect_skills(agent, processes, skills_dir)
    target = os.path.join(PLUGINS_DIR, agent["slug"])
    if os.path.isdir(target):
        shutil.rmtree(target)

    write(
        os.path.join(target, "plugin.json"),
        json.dumps(
            manifest(agent, processes), indent=2, ensure_ascii=False
        )
        + "\n",
    )
    write(os.path.join(target, "README.md"), readme_page(agent, skills))
    write(os.path.join(target, NAMESPACE, "RECORDS.md"), records_page(agent))
    write(os.path.join(target, NAMESPACE, "SERVERS.md"), servers_page(agent))
    write(os.path.join(target, NAMESPACE, "NOT.md"), not_page(agent))
    for skill in skills:
        write(
            os.path.join(target, "skills", skill["slug"], "SKILL.md"),
            skill_page(agent, skill),
        )
    return skills


def main():
    process_paths = []
    for folder, _, names in os.walk(PROCESSES_DIR):
        process_paths += [
            os.path.join(folder, n) for n in names if n.endswith(".md")
        ]
    processes = {}
    for path in sorted(process_paths):
        process = read_process(path)
        processes[process["id"]] = process

    agent_paths = sorted(
        os.path.join(AGENTS_DIR, n)
        for n in os.listdir(AGENTS_DIR)
        if n.endswith(".md")
    )

    os.makedirs(PLUGINS_DIR, exist_ok=True)
    counts, problems = {}, []
    for path in agent_paths:
        agent = read_agent(path, processes)
        for problem in agent["problems"]:
            problems.append("%s: %s" % (agent["slug"], problem))
        counts[agent["slug"]] = len(build(agent, processes, SKILLS_DIR))

    total = sum(counts.values())
    smallest = min(counts.items(), key=lambda pair: (pair[1], pair[0]))
    largest = min(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    print("read %d reference processes" % len(processes))
    print("wrote %d plugin packages into %s" % (len(counts), PLUGINS_DIR))
    print("wrote %d skills in total" % total)
    print("fewest: %s with %d" % (smallest[0], smallest[1]))
    print("most:   %s with %d" % (largest[0], largest[1]))
    if problems:
        print("\n%d documents did not parse cleanly:" % len(problems))
        for problem in problems:
            print("  " + problem)
        return 1
    print("every document parsed cleanly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
