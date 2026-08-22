---
name: put-a-statement-in-front-of-every-seller
description: Takes the approved carve, builds each seller a statement of the patch they hold and the number on it, releases them all on one date, and opens the window in which a seller may appeal. Use it when running `ref/rev/publish-the-carve`.
license: CC-BY-4.0
metadata:
  agent: quota-setter
  agent-version: "1"
---

# Put a statement in front of every seller

## What it does

Takes the approved carve, builds each seller a statement of the patch
they hold and the number on it, releases them all on one date, and opens
the window in which a seller may appeal.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Build a Statement per Seller**
  - `ref/rev/publish-the-carve`, activity 3 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Open the Appeal Window**
  - `ref/rev/publish-the-carve`, activity 8 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Release the Statements**
  - `ref/rev/publish-the-carve`, activity 7 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Take in the Approved Carve**
  - `ref/rev/publish-the-carve`, activity 1 -
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
