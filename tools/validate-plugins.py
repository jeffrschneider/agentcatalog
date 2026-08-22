#!/usr/bin/env python3
"""Check the Agent Plugin packages under plugins/ before they are published.

Each package is one abstract agent written as an Agent Plugin. This script
reads every package, reports what is wrong with it and where, and exits 0
when everything passes or 1 when anything fails.

    python tools/validate-plugins.py
    python tools/validate-plugins.py --quiet
    python tools/validate-plugins.py /some/plugins --processes /some/processes

It uses only the Python standard library, so CI can run it with a plain
Python and no install step.
"""

import argparse
import json
import os
import re
import sys

EXTENSION = "com.agentcatalog.agent"
SCHEMA_URL = "https://agent-plugins.org/schemas/1.1.0/plugin.schema.json"
SIDECARS = ("RECORDS.md", "SERVERS.md", "NOT.md")
# An agent either reads a system, writes to it, or sets something in it
# running without reading or writing what is there. Ten of the agent documents
# grant that third kind: the live sends, the staged releases, the scheduled
# price changes. It is a real access level and not a typo for write.
ACCESS_LEVELS = ("read", "write", "trigger")

SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PROCESS_REF = re.compile(r"^ref/[a-z0-9-]+/[a-z0-9-]+$")
PROCESS_ID_IN_DOC = re.compile(r"^`(ref/[a-z0-9-]+/[a-z0-9-]+)\s+v\d+`\s*$", re.MULTILINE)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
RETIRED_WORD = re.compile(r"seat", re.IGNORECASE)

BLOCK_MARKERS = ("|", ">", "|-", ">-", "|+", ">+")
MAX_TEXT_HITS = 5


# ---------------------------------------------------------------- helpers


def relative(path, base):
    """Path of a file inside a package, written with forward slashes."""
    return os.path.relpath(path, base).replace(os.sep, "/")


def read_text(path):
    """Read a file as UTF-8. Returns a pair, and one half of it is None."""
    try:
        with open(path, "rb") as handle:
            raw = handle.read()
    except OSError as err:
        return None, "cannot be read: %s" % err
    try:
        return raw.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, "is not UTF-8 text, and a package should hold only text files"


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text):
    """Read the top level keys out of a YAML frontmatter block.

    Nested mappings are skipped, because nothing here needs to look
    inside them.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "does not start with a --- frontmatter block"

    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break
    if end is None:
        return None, "has a frontmatter block that is never closed with a second ---"

    fields = {}
    key = None
    collecting = False
    for raw in lines[1:end]:
        stripped = raw.strip()
        if not stripped:
            continue
        if raw[0] in " \t":
            # An indented line either continues the value above or belongs
            # to a nested mapping, which this parser does not read.
            if collecting and key is not None:
                fields[key] = (fields[key] + " " + stripped).strip()
            continue
        match = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", raw)
        if not match:
            key, collecting = None, False
            continue
        key = match.group(1)
        value = match.group(2).strip()
        if value in BLOCK_MARKERS:
            fields[key] = ""
            collecting = True
        elif value == "":
            fields[key] = ""
            collecting = False
        else:
            fields[key] = unquote(value)
            collecting = True
    return fields, None


def load_process_index(processes_dir):
    """Map every reference process id to the file that defines it.

    A process document names its own id on a line of its own, like
    `ref/mkt/lead-routing v1`, and that line is what a plugin points at.
    The department in the id is not the same word as the directory it
    lives in, so the ids are read from the documents rather than guessed
    from the paths.
    """
    index = {}
    problems = []
    for root, dirs, files in os.walk(processes_dir):
        dirs.sort()
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            text, error = read_text(path)
            if text is None:
                problems.append("%s %s" % (relative(path, processes_dir), error))
                continue
            match = PROCESS_ID_IN_DOC.search(text)
            if not match:
                continue
            process_id = match.group(1)
            if process_id in index and index[process_id] != path:
                problems.append(
                    "%s claims the id %s, which %s already claims"
                    % (
                        relative(path, processes_dir),
                        process_id,
                        relative(index[process_id], processes_dir),
                    )
                )
                continue
            index[process_id] = path
    return index, problems


# ----------------------------------------------------------- field checks


def is_text(value):
    return isinstance(value, str) and value.strip() != ""


def kind_of(value):
    """Say what a value is, in words, for a message about the wrong type."""
    if value is None:
        return "missing"
    if isinstance(value, bool):
        return "a true or false value"
    if isinstance(value, (int, float)):
        return "a number"
    if isinstance(value, str):
        return "an empty string" if value.strip() == "" else "a string"
    if isinstance(value, list):
        return "a list"
    if isinstance(value, dict):
        return "an object"
    return "a %s" % type(value).__name__


def check_string_list(problems, at, field, value):
    """A field that has to be a list of non-empty strings with entries in it."""
    if not isinstance(value, list):
        problems.append('%s: "%s" must be a list, and it is %s' % (at, field, kind_of(value)))
        return
    if not value:
        problems.append('%s: "%s" is an empty list, and it needs at least one entry' % (at, field))
        return
    for position, entry in enumerate(value):
        if not is_text(entry):
            problems.append(
                '%s: "%s" entry %d must be a non-empty string, and it is %s'
                % (at, field, position + 1, kind_of(entry))
            )


def check_plugin_json(problems, package_dir, slug, process_index):
    """Read plugin.json and check the parts the catalog depends on."""
    path = os.path.join(package_dir, "plugin.json")
    where = "plugin.json"
    if not os.path.isfile(path):
        problems.append("plugin.json: the file is missing")
        return 0

    text, error = read_text(path)
    if text is None:
        problems.append("%s: %s" % (where, error))
        return 0
    try:
        data = json.loads(text)
    except ValueError as err:
        problems.append("%s: the file is not valid JSON (%s)" % (where, err))
        return 0
    if not isinstance(data, dict):
        problems.append("%s: the top level must be an object, and it is %s" % (where, kind_of(data)))
        return 0

    schema = data.get("$schema")
    if schema != SCHEMA_URL:
        problems.append(
            '%s: "$schema" must be "%s", and it is %s'
            % (where, SCHEMA_URL, json.dumps(schema) if schema is not None else "missing")
        )

    for field in ("name", "version", "description"):
        if not is_text(data.get(field)):
            problems.append(
                '%s: "%s" must be a non-empty string, and it is %s'
                % (where, field, kind_of(data.get(field)))
            )

    name = data.get("name")
    if is_text(name) and name != slug:
        problems.append(
            '%s: "name" is "%s" but the directory is "%s", and the two must match'
            % (where, name, slug)
        )

    version = data.get("version")
    if is_text(version) and not SEMVER.match(version):
        problems.append(
            '%s: "version" is "%s", which is not a semantic version like 1.0.0' % (where, version)
        )

    return check_extension(problems, where, data, slug, process_index)


def check_extension(problems, where, data, slug, process_index):
    """Check the com.agentcatalog.agent block and return the process count."""
    extensions = data.get("extensions")
    if not isinstance(extensions, dict):
        problems.append('%s: "extensions" must be an object, and it is %s' % (where, kind_of(extensions)))
        return 0
    extension = extensions.get(EXTENSION)
    if not isinstance(extension, dict):
        problems.append(
            '%s: the "%s" extension must be an object, and it is %s'
            % (where, EXTENSION, kind_of(extension))
        )
        return 0

    at = "%s extensions.%s" % (where, EXTENSION)

    agent = extension.get("agent")
    if not is_text(agent):
        problems.append('%s: "agent" must be a non-empty string, and it is %s' % (at, kind_of(agent)))
    elif agent != slug:
        problems.append(
            '%s: "agent" is "%s" but the directory is "%s", and the two must match' % (at, agent, slug)
        )

    agent_version = extension.get("agentVersion")
    if isinstance(agent_version, bool) or not isinstance(agent_version, int):
        problems.append(
            '%s: "agentVersion" must be a whole number, and it is %s' % (at, kind_of(agent_version))
        )
    elif agent_version < 1:
        problems.append('%s: "agentVersion" is %d, and it must be 1 or greater' % (at, agent_version))

    if extension.get("abstract") is not True:
        problems.append(
            '%s: "abstract" must be true, and it is %s'
            % (at, json.dumps(extension.get("abstract")) if "abstract" in extension else "missing")
        )

    for field in ("department", "works"):
        if not is_text(extension.get(field)):
            problems.append(
                '%s: "%s" must be a non-empty string, and it is %s'
                % (at, field, kind_of(extension.get(field)))
            )

    check_servers(problems, at, extension.get("servers"))
    for field in ("records", "escalates", "not"):
        check_string_list(problems, at, field, extension.get(field))
    return check_processes(problems, at, extension.get("processes"), process_index)


def check_servers(problems, at, servers):
    if not isinstance(servers, list):
        problems.append('%s: "servers" must be a list, and it is %s' % (at, kind_of(servers)))
        return
    if not servers:
        problems.append('%s: "servers" is empty, and an agent that reaches no system has nothing to do' % at)
        return
    for position, server in enumerate(servers):
        label = '%s: "servers" entry %d' % (at, position + 1)
        if not isinstance(server, dict):
            problems.append("%s must be an object, and it is %s" % (label, kind_of(server)))
            continue
        if not is_text(server.get("role")):
            problems.append('%s has no "role", and every server entry needs one' % label)
        else:
            label = '%s: server "%s"' % (at, server["role"])
        access = server.get("access")
        if access not in ACCESS_LEVELS:
            problems.append(
                "%s has access %s, and access must be %s"
                % (
                    label,
                    json.dumps(access) if access is not None else "missing",
                    ", ".join('"%s"' % a for a in ACCESS_LEVELS),
                )
            )
        for field in ("needs", "example"):
            if field in server and not is_text(server.get(field)):
                problems.append(
                    '%s has a "%s" that is %s, and it must be a non-empty string'
                    % (label, field, kind_of(server.get(field)))
                )


def check_processes(problems, at, processes, process_index):
    """Check every process reference, including that it points at a real file."""
    if not isinstance(processes, list):
        problems.append('%s: "processes" must be a list, and it is %s' % (at, kind_of(processes)))
        return 0
    if not processes:
        problems.append(
            '%s: "processes" is empty, and an agent holds activities in at least one process' % at
        )
        return 0

    seen = set()
    for position, entry in enumerate(processes):
        label = '%s: "processes" entry %d' % (at, position + 1)
        if not isinstance(entry, dict):
            problems.append("%s must be an object, and it is %s" % (label, kind_of(entry)))
            continue
        process_id = entry.get("process")
        if not is_text(process_id):
            problems.append('%s has no "process" id' % label)
        else:
            label = '%s: process "%s"' % (at, process_id)
            if not PROCESS_REF.match(process_id):
                problems.append("%s is not shaped like ref/<department>/<slug>" % label)
            elif process_id not in process_index:
                problems.append("%s does not match any document in the processes directory" % label)
            if process_id in seen:
                problems.append("%s is listed more than once" % label)
            seen.add(process_id)
        activities = entry.get("activities")
        if not isinstance(activities, list):
            problems.append(
                '%s has an "activities" field that is %s, and it must be a list'
                % (label, kind_of(activities))
            )
            continue
        if not activities:
            problems.append("%s lists no activities, so the reference says nothing" % label)
        for activity in activities:
            if not is_text(activity):
                problems.append(
                    "%s has an activity that is %s, and it must be a non-empty string"
                    % (label, kind_of(activity))
                )
    return len(processes)


def check_skills(problems, package_dir):
    """Every skill directory needs a SKILL.md whose name matches the directory."""
    skills_dir = os.path.join(package_dir, "skills")
    if not os.path.isdir(skills_dir):
        problems.append("skills/: the directory is missing, and a package carries at least one skill")
        return 0

    slugs = sorted(
        name for name in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, name))
    )
    if not slugs:
        problems.append("skills/: the directory holds no skills")
        return 0

    for slug in slugs:
        where = "skills/%s" % slug
        if not SLUG.match(slug):
            problems.append("%s: the directory name is not a lowercase slug like score-lead" % where)
        skill_path = os.path.join(skills_dir, slug, "SKILL.md")
        if not os.path.isfile(skill_path):
            problems.append("%s/SKILL.md: the file is missing" % where)
            continue
        text, error = read_text(skill_path)
        if text is None:
            problems.append("%s/SKILL.md: %s" % (where, error))
            continue
        if not text.strip():
            problems.append("%s/SKILL.md: the file is empty" % where)
            continue
        fields, error = parse_frontmatter(text)
        if fields is None:
            problems.append("%s/SKILL.md: %s" % (where, error))
            continue
        name = fields.get("name")
        if not is_text(name):
            problems.append('%s/SKILL.md: the frontmatter has no "name"' % where)
        elif name != slug:
            problems.append(
                '%s/SKILL.md: the frontmatter name is "%s" but the directory is "%s", '
                "and the two must match" % (where, name, slug)
            )
        if not is_text(fields.get("description")):
            problems.append('%s/SKILL.md: the frontmatter has no "description"' % where)
    return len(slugs)


def check_sidecars(problems, package_dir):
    """The three files that say what the agent records, needs, and never does."""
    folder = os.path.join(package_dir, EXTENSION)
    if not os.path.isdir(folder):
        problems.append("%s/: the directory is missing" % EXTENSION)
        return
    for name in SIDECARS:
        path = os.path.join(folder, name)
        where = "%s/%s" % (EXTENSION, name)
        if not os.path.isfile(path):
            problems.append("%s: the file is missing" % where)
            continue
        text, error = read_text(path)
        if text is None:
            problems.append("%s: %s" % (where, error))
        elif not text.strip():
            problems.append("%s: the file is empty" % where)


def check_readme(problems, package_dir):
    path = os.path.join(package_dir, "README.md")
    if not os.path.isfile(path):
        problems.append("README.md: the file is missing")
        return
    text, error = read_text(path)
    if text is None:
        problems.append("README.md: %s" % error)
    elif not text.strip():
        problems.append("README.md: the file is empty")


def count_of(number, word, plural=None):
    """Write a count in words, so the report reads as a sentence."""
    if number == 1:
        return "%d %s" % (number, word)
    return "%d %s" % (number, plural or word + "s")


def snippet(line, position, width=44):
    start = max(0, position - 14)
    return line[start:start + width].strip()


def check_text_of_every_file(problems, package_dir):
    """Look through every file for the retired word and for email addresses.

    The word "seat" was the old name for an abstract agent and is being
    retired, so it must not appear anywhere in a package. An email address
    must not appear because this repository is public.
    """
    retired = []
    emails = []
    for root, dirs, files in os.walk(package_dir):
        dirs.sort()
        for name in sorted(dirs) + sorted(files):
            if RETIRED_WORD.search(name):
                path = os.path.join(root, name)
                retired.append(
                    '%s: the retired word "seat" is in the name of this file or directory'
                    % relative(path, package_dir)
                )
        for name in sorted(files):
            path = os.path.join(root, name)
            where = relative(path, package_dir)
            text, error = read_text(path)
            if text is None:
                problems.append("%s: %s" % (where, error))
                continue
            for number, line in enumerate(text.splitlines(), start=1):
                match = RETIRED_WORD.search(line)
                if match:
                    retired.append(
                        '%s line %d: the retired word "seat" appears, in "%s"'
                        % (where, number, snippet(line, match.start()))
                    )
                for match in EMAIL.finditer(line):
                    emails.append(
                        "%s line %d: an email address appears (%s), and this repository is public"
                        % (where, number, match.group(0))
                    )

    for found in (retired, emails):
        for message in found[:MAX_TEXT_HITS]:
            problems.append(message)
        if len(found) > MAX_TEXT_HITS:
            problems.append("and %d more of the same kind" % (len(found) - MAX_TEXT_HITS))


def check_package(package_dir, slug, process_index):
    problems = []
    process_count = check_plugin_json(problems, package_dir, slug, process_index)
    skill_count = check_skills(problems, package_dir)
    check_sidecars(problems, package_dir)
    check_readme(problems, package_dir)
    check_text_of_every_file(problems, package_dir)
    return problems, skill_count, process_count


# ------------------------------------------------------------------ main


def parse_args(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(here)
    parser = argparse.ArgumentParser(
        description="Check the Agent Plugin packages under plugins/."
    )
    parser.add_argument(
        "plugins",
        nargs="?",
        default=os.path.join(repo, "plugins"),
        help="the directory that holds the packages, which is the plugins directory of this repository by default",
    )
    parser.add_argument(
        "--processes",
        default=os.path.join(repo, "processes"),
        help="the directory that holds the reference process documents",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print only the failures and the final tally",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    plugins_dir = os.path.abspath(args.plugins)
    processes_dir = os.path.abspath(args.processes)

    if not os.path.isdir(plugins_dir):
        print("There is no directory at %s, so there is nothing to check." % plugins_dir)
        return 0

    packages = sorted(
        name for name in os.listdir(plugins_dir) if os.path.isdir(os.path.join(plugins_dir, name))
    )
    if not packages:
        print("There are no packages in %s, so there is nothing to check." % plugins_dir)
        return 0

    if not os.path.isdir(processes_dir):
        print(
            "There is no directory at %s, and the process references cannot be checked without it."
            % processes_dir
        )
        return 1

    process_index, index_problems = load_process_index(processes_dir)
    for problem in index_problems:
        print("processes: %s" % problem)
    if not process_index:
        print(
            "No reference process ids were found in %s, so no package can be checked against them."
            % processes_dir
        )
        return 1

    if not args.quiet:
        print("Checking %s in %s" % (count_of(len(packages), "package"), plugins_dir))
        print(
            "against %s in %s."
            % (
                count_of(len(process_index), "reference process", "reference processes"),
                processes_dir,
            )
        )
        print("")

    passed = 0
    failed = 0
    for slug in packages:
        package_dir = os.path.join(plugins_dir, slug)
        problems, skill_count, process_count = check_package(package_dir, slug, process_index)
        if problems:
            failed += 1
            print("%s FAILED" % slug)
            for problem in problems:
                print("    %s" % problem)
        else:
            passed += 1
            if not args.quiet:
                print(
                    "%s passed, with %s and %s"
                    % (
                        slug,
                        count_of(skill_count, "skill"),
                        count_of(process_count, "process reference"),
                    )
                )

    print("")
    print(
        "Checked %s. %d passed, %d failed."
        % (count_of(len(packages), "package"), passed, failed)
    )
    return 1 if failed or index_problems else 0


if __name__ == "__main__":
    sys.exit(main())
