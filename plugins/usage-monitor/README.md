# usage-monitor

This is an abstract agent, published as an Agent Plugin. An abstract
agent is a job description rather than an implementation. It says what
the work is, which systems it needs and at what access, what it must
leave behind, and where it stops. Any agent that leaves the records can
implement it.

The plugin carries five skills, no `mcp.json`, and everything the
abstract agent owes under `com.agentcatalog.agent/`.

## Why there is no mcp.json

A conformant server entry in `mcp.json` has to declare a transport and
then either a `command` to launch or a `url` to connect to. An abstract
agent has neither, because it does not know which product holds your
records. Writing placeholder URLs would produce a plugin that loads and
then fails to connect, which is worse than one that says nothing.

Section 6.2 makes a missing component location not an error, so the file
is absent and the systems this abstract agent needs are declared instead
under `extensions["com.agentcatalog.agent"].servers`, as a role, an
access level and what the access is for. Whoever builds an agent from
this plugin writes the `mcp.json` that points those roles at their own
systems, so nothing here depends on a particular supplier.

## Why the obligations are in an extension

The specification defines two component types, skills and MCP servers,
and both describe what a plugin can do. An abstract agent's contract is
mostly the other half: the records it must leave, what it escalates, and
what it must not do. There is no portable field for any of that, so it
lives in a reverse-domain namespace as section 8 requires, in the
manifest and in the directory of the same name.

## Where this abstract agent is used

`ref/sls/spot-an-expansion`, `ref/sls/open-an-expansion-deal`,
`ref/sls/open-a-renewal`, `ref/sls/close-a-renewal`,
`ref/sls/work-a-churn-risk`. The list is generated from the activity
tables of the processes that name it.

https://agentcatalog.com/abstract-agents/usage-monitor
