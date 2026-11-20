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
- **The roles**, split into the ones an agent can hold (each citing an
  [abstract agent](./abstract-agent.md)) and the ones only a person
  holds.
- **The handoffs and the failure edges**, because they come with the
  shape of the work.
- **The records** a run must leave.
- **The goals**, in a section of their own between the summary and the
  activities: three or four things a company wants from running the
  process again and again, chosen so they pull against each other, so
  that pushing one too hard shows what it costs the others. A process
  never has a single goal. Each goal carries one suggested target in
  square brackets, such as "Win [35%] of proposals sent", and the target
  is a suggestion for you to change. These are business goals across
  runs. The document's `goal:` line says something else: what is true
  when one run closes.
- **What it delivers**, on a `**delivers:**` line of its own between the
  summary and the goals: the kind of thing a run leaves in somebody's
  hands, in one of fifteen words: document, verdict, status board,
  sheet, report, page, agreement, campaign, shortlist, statement, deal,
  creative set, sequence, notes or event. A comma and the deliverable's
  own name follow, short and plain, such as `**delivers:** verdict, a
  mandate check`. Both are read from the `goal:` line, and a gallery
  uses them to picture the process as the thing it produces. A proposal is a document and a calendar is a sheet. A
  process whose run leaves a system changed, such as merging duplicate
  records, delivers a status board.
- **How it starts**, on a `**starts:**` line of its own after the
  delivers line: one of three ways a run begins, then a comma and the
  process's own words for what begins it, taken from the trigger node of
  its graph, such as `**starts:** on a schedule, a reporting period
  ends`. The three ways are:
  - **on a schedule**: a date or a period on your own calendar comes
    round, such as a month closing or a review falling due;
  - **on an event**: something happens that a system records, such as a
    record changing, a message or a document arriving from outside the
    company, or another process handing its work on;
  - **by hand**: a person in the company asks for the work, proposes it
    or decides on it.

  A process names one way, the one its `trigger:` line names first. It
  is read from that line: a `watch: every=` or a date on your calendar
  is a schedule, a person here asking is by hand, and anything else is
  an event. Whatever the line says, a person can always run the process
  now, so a trigger whose second way in is someone asking still names
  its timer or its watch.

## What stays blank

- The **owner** and the **effective date** - a reference process has
  neither, and that is the mark that it is not yet anyone's process.
- The **roster** - which agent or person actually holds each role.
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
