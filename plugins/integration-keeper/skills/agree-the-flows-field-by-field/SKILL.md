---
name: agree-the-flows-field-by-field
description: Names the system on each side with the person who owns it, agrees every field that moves with its direction, its cadence and what starts the move, and gets a decision on which side is right where the two owners disagree. Use it when running `ref/rev/integrate-a-tool`.
license: CC-BY-4.0
metadata:
  agent: integration-keeper
  agent-version: "1"
---

# Agree the flows field by field

## What it does

Names the system on each side with the person who owns it, agrees every
field that moves with its direction, its cadence and what starts the
move, and gets a decision on which side is right where the two owners
disagree.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Agree What Flows Where**
  - `ref/rev/integrate-a-tool`, activity 3 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Decide Which Side Wins**
  - `ref/rev/integrate-a-tool`, activity 5 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Name the Systems Either Side**
  - `ref/rev/integrate-a-tool`, activity 2 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)

## What to record

Per link: the systems either side with the person who owns each, the
agreed flows at a version naming every field, its direction, its cadence
and what starts the move, and the system of record per field with who
decided where the owners could not agree. The known set moved through
the link with the counts on both sides, field by field, and every
difference. The failure test, saying what the link retried, duplicated,
dropped and queued when it was broken on purpose. The cleared review
with the date it was signed and every finding accepted rather than
fixed. The date and hour it went live, and the way back as it was
written down before the switch. The first runs and the reconciled
counts, dated, with the reason behind every difference where one is
known. The record of what flows where at its version, naming the fields
it does not yet cover. When a link stops, what it was carrying and where
that now comes from.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
