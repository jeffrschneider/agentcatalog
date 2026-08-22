---
name: move-a-process-out-of-a-tool-that-is-going
description: Takes a decision to retire, names where the work goes next, sees it moved there, and files what the retirement taught. Use it when running `ref/rev/retire-a-tool`.
license: CC-BY-4.0
metadata:
  agent: stack-planner
  agent-version: "1"
---

# Move a process out of a tool that is going

## What it does

Takes a decision to retire, names where the work goes next, sees it
moved there, and files what the retirement taught. The tool stays on
until a home is named and somebody has agreed to take the work.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Move the Process to Its New Home**
  - `ref/rev/retire-a-tool`, activity 6 -
    [Retire a Tool](../../../../processes/revenue-operations/retire-a-tool.md)
- **Name Where the Process Goes**
  - `ref/rev/retire-a-tool`, activity 3 -
    [Retire a Tool](../../../../processes/revenue-operations/retire-a-tool.md)
- **Record What Was Learned**
  - `ref/rev/retire-a-tool`, activity 15 -
    [Retire a Tool](../../../../processes/revenue-operations/retire-a-tool.md)
- **Take in the Decision to Retire**
  - `ref/rev/retire-a-tool`, activity 1 -
    [Retire a Tool](../../../../processes/revenue-operations/retire-a-tool.md)

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
