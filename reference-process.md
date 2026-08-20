# Writing down a reference process

A reference process is a process document with the organizational parts
left blank. It uses the same format as
[Agent Processes](https://github.com/jeffrschneider/agentprocesses/blob/main/process.md),
and it stands to your process the way a work pattern stands to a work
plan: the shape is filled in, the specifics are yours to supply. You
copy it, fill in the header and the bindings, and it becomes your
process at version 1 with your name on it.

The family already draws this line once. A work pattern is generic
because its shape recurs across organizations; a process is yours
because it carries your owner, your systems, your gates. A reference
process sits between the two on purpose: it is shaped like a process,
generic like a pattern, and it never claims to be running anywhere.

## What is filled in

- **The activities**, each with a name, a plain description, and the
  roles involved. This is the part that took the work: someone said out
  loud how the work gets done, turned it into a table, and drew the
  graph. Adopting the reference process means you inherit that walk
  instead of doing it from scratch.
- **The graph** - the `after:` lines, the branches, the backward edges.
- **The roles**, split into seats an agent can hold (each citing an
  [abstract agent](./abstract-agent.md)) and seats only a person holds.
- **The handoffs and the failure edges**, because they come with the
  shape of the work.
- **The records** a run must leave.

## What stays blank

- The **owner** and the **effective date** - a reference process has
  neither, and that is the mark that it is not yet anyone's process.
- The **roster** - which agent or person actually holds each seat.
- The **caps and thresholds** - spend limits, deadlines, escalation
  numbers. The reference process shows where a number goes; the number
  is your decision.
- The **policy specifics** - the reference process carries the generic
  rule ("nothing publishes unsigned"); your regulators, contracts and
  brand decide the rest.
- The **measures targets** - the reference process names what to
  measure; the targets are yours.

## Ids and adoption

Reference processes are cited as `ref/<domain>/<slug>`, for example
`ref/mkt/social-campaign`. When an organization adopts one, their
document takes their own id and records where it came from:

```
PROCESS: social campaign              id: acme-mkt/social-campaign   v1
from: ref/mkt/social-campaign v1
```

The `from:` line is provenance rather than dependency. Once adopted,
your document is yours: you amend it from your own debriefs, and the
reference process never reaches into it. If your amendments teach the
reference process something every adopter needs, that flows back as a
new version of the reference process, the same way a plan that keeps
being copied becomes a work pattern.

## What a reference process is not

It is not a best practice. It is a first draft to argue with - the value
is that the activity walk is already done, and the argument starts from
a complete picture instead of a blank page.

It is not running anywhere. It has no owner, no runs, no records, and a
catalog that listed reference processes as `running` would be one people
stop believing.
