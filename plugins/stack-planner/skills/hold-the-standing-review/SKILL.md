---
name: hold-the-standing-review
description: Holds the review that asks whether a tool still earns its place, and records the decision with its date, the evidence it was made on and the date the next one falls. Use it when running `ref/rev/administer-a-tool`.
license: CC-BY-4.0
metadata:
  agent: stack-planner
  agent-version: "1"
---

# Hold the standing review

## What it does

Holds the review that asks whether a tool still earns its place, and
records the decision with its date, the evidence it was made on and the
date the next one falls. A review that did not happen is recorded as not
held rather than left blank.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record the Review**
  - `ref/rev/administer-a-tool`, activity 15 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)
- **Run the Standing Review**
  - `ref/rev/administer-a-tool`, activity 13 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)

## What to record

Per run: the need as the requester stated it, the process named as the
one that would run inside the tool, and what the stack already holds
that comes near, with what each of those falls short on. The
requirements and the criteria at their fixed version with the date they
were fixed, and every later change carried as a new version marking the
scores made against the earlier one. The shortlist, with the requirement
each dropped candidate failed. The trial result for each finalist on the
same work over the same period, with the figures and the range around
each. The whole cost, the comparison against one list, and the decision
naming who chose, when and why. The stack entry itself, and for a
retirement the closed entry with what replaced it and where the kept
data now sits. Each standing review lands with its decision, its date,
the evidence it was made on and the date the next one falls, and a
review that did not happen is recorded as not held rather than left
blank.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
