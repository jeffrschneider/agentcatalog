---
name: narrow-the-field-to-finalists
description: Works the market down to a shortlist, naming the requirement each dropped candidate failed. Use it when running `ref/rev/choose-a-tool`.
license: CC-BY-4.0
metadata:
  agent: stack-planner
  agent-version: "1"
---

# Narrow the field to finalists

## What it does

Works the market down to a shortlist, naming the requirement each
dropped candidate failed. Runs the finalists on the work the team really
has, over the same period, adds up what each one costs over its term,
and sets them side by side against one list.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Compare the Finalists**
  - `ref/rev/choose-a-tool`, activity 16 -
    [Choose a Tool](../../../../processes/revenue-operations/choose-a-tool.md)
- **Cut to a Shortlist**
  - `ref/rev/choose-a-tool`, activity 9 -
    [Choose a Tool](../../../../processes/revenue-operations/choose-a-tool.md)
- **Search the Market**
  - `ref/rev/choose-a-tool`, activity 8 -
    [Choose a Tool](../../../../processes/revenue-operations/choose-a-tool.md)
- **Trial the Finalists on Real Work**
  - `ref/rev/choose-a-tool`, activity 13 -
    [Choose a Tool](../../../../processes/revenue-operations/choose-a-tool.md)
- **Work out the Whole Cost**
  - `ref/rev/choose-a-tool`, activity 14 -
    [Choose a Tool](../../../../processes/revenue-operations/choose-a-tool.md)

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
