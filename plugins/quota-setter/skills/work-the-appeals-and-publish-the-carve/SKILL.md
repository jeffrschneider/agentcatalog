---
name: work-the-appeals-and-publish-the-carve
description: Applies what the appeals changed, publishes the final carve, and records what the appeals showed, because the same argument arriving twice is a fault in the carve rather than in the seller. Use it when running `ref/rev/publish-the-carve`.
license: CC-BY-4.0
metadata:
  agent: quota-setter
  agent-version: "1"
---

# Work the appeals and publish the carve

## What it does

Applies what the appeals changed, publishes the final carve, and records
what the appeals showed, because the same argument arriving twice is a
fault in the carve rather than in the seller.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Apply What Changed**
  - `ref/rev/publish-the-carve`, activity 12 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Publish the Final Carve**
  - `ref/rev/publish-the-carve`, activity 13 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Record What the Appeals Showed**
  - `ref/rev/publish-the-carve`, activity 15 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)

## What to record

Per run: the over-assignment as a figure with who decided it and why, a
draft on every patch naming the carrying figure and the curve behind it,
and the capacity test and the history test attached to each number.
Every number further from history than the stated distance carries the
reason for the difference beside it. The roll-up states the sum, the
target and the distance between them as an amount, and any adjustment
records what moved, on which patch, and by how much. Ramped numbers name
the written rule that produced them and the dates they cover. The signed
set names the person who signed it and the hour, and a quota changed
afterwards is a new version saying what moved and who decided it, with
the version it replaces left where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
