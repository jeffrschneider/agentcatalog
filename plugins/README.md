# Plugins

This directory holds one package for each abstract agent in the catalog.
Each package is an abstract agent written as an Agent Plugin, following
version 1.1.0 of the Agent Plugins specification.

An abstract agent is a description of a job. It says what the work is,
which systems the agent needs and at what level of access, what records it
has to leave behind, and where it stops. It says nothing about which
product you should buy or which vendor you should hire, because those are
your decisions.

## How you use one

You build your own agent from a package by pointing its servers at your
own systems. No vendor is involved. The package names
each system it needs by role, such as a contact record or a notification
channel, and says whether the agent reads from that system or writes to
it. You choose the product that fills each role, you write the `mcp.json`
that connects them, and the agent you end up with is yours.

That is also why a package carries no `mcp.json` of its own. The package
cannot know whether your contact record lives in Salesforce or HubSpot,
and a placeholder connection would load and then fail to connect, which
is worse than saying nothing.

## What is in a package

    plugins/<agent>/
      plugin.json
      README.md
      skills/<skill>/SKILL.md
      com.agentcatalog.agent/RECORDS.md
      com.agentcatalog.agent/SERVERS.md
      com.agentcatalog.agent/NOT.md

`plugin.json` is the manifest. Everything the abstract agent owes sits in
it under `extensions["com.agentcatalog.agent"]`: the department, the
systems it needs, the records it must leave, what it escalates and to
whom, what it never does, and the activities it holds in the reference
processes under `processes/`.

`skills/` holds one skill for each capability the agent has: one thing it
knows how to do. A capability usually covers several activities, because
the reference processes name the same work differently depending on what
it is being done to. Watching the first weeks of a launch and watching the
registrations for a webinar are one capability with two names, so they are
one skill, and the skill lists every activity it covers.

The three files under `com.agentcatalog.agent/` say the same things in
prose, for a person who is deciding whether to deploy the agent. Read
`SERVERS.md` to see what you would have to give it access to, `RECORDS.md`
to see what it will leave behind, and `NOT.md` to see where it stops.

## Where the packages come from

Every package is generated from the agent document of the same name in
`agents/`. Nobody edits a package by hand. When a package says something
wrong, the fix belongs in `agents/<agent>.md`, and the package is
generated again from there. An edit made in this directory is lost the
next time the generator runs.

## How the packages are checked

Run `python tools/validate-plugins.py` to read every package here. It
checks that the manifest is complete and correctly typed, that each skill
matches its directory, that the three files above are present and have
something in them, and that every reference process a package points at is
a real document in `processes/`. A package that names a process the
catalog does not have is a failure, which is what keeps these packages
honest against the rest of the repository. The same check runs in CI on
every push and every pull request.
