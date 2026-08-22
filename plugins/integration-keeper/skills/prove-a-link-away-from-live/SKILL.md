---
name: prove-a-link-away-from-live
description: Builds the link where no real record is written, moves a known set and counts both sides field by field, and breaks the link on purpose to see what it retries, duplicates, drops and queues. Use it when running `ref/rev/administer-a-tool` and `ref/rev/integrate-a-tool`.
license: CC-BY-4.0
metadata:
  agent: integration-keeper
  agent-version: "1"
---

# Prove a link away from live

## What it does

Builds the link where no real record is written, moves a known set and
counts both sides field by field, and breaks the link on purpose to see
what it retries, duplicates, drops and queues. A change to a link
already running is tried the same way.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Link away from Live**
  - `ref/rev/integrate-a-tool`, activity 7 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Move a Known Set and Compare**
  - `ref/rev/integrate-a-tool`, activity 8 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Test What Happens When It Breaks**
  - `ref/rev/integrate-a-tool`, activity 9 -
    [Integrate a Tool](../../../../processes/revenue-operations/integrate-a-tool.md)
- **Try the Change away from Live**
  - `ref/rev/administer-a-tool`, activity 6 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)

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
