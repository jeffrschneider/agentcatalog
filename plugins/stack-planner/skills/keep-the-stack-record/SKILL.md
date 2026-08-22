---
name: keep-the-stack-record
description: Writes the chosen tool into the stack record and keeps that record true afterwards, so every entry names the process it serves, its owner, its cost, its term and its renewal date. Use it when running `ref/rev/choose-a-tool`, `ref/rev/integrate-a-tool` and `ref/rev/retire-a-tool`.
license: CC-BY-4.0
metadata:
  agent: stack-planner
  agent-version: "1"
---

# Keep the stack record

## What it does

Writes the chosen tool into the stack record and keeps that record true
afterwards, so every entry names the process it serves, its owner, its
cost, its term and its renewal date. A retirement closes an entry with
what replaced it rather than removing it.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Take in the Chosen Tool**
  - `ref/rev/integrate-a-tool`, activity 1 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Update the Stack Record**
  - `ref/rev/retire-a-tool`, activity 14 -
    [Retire a Tool](../../../../processes/revenue-operations/retire-a-tool.md)
- **Write It into the Stack Record**
  - `ref/rev/choose-a-tool`, activity 18 -
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
