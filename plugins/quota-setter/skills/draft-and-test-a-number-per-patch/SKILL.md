---
name: draft-and-test-a-number-per-patch
description: Drafts a number on every patch from the carrying model and the attainment curve, tests each one against the capacity behind it and against what that patch actually closed, works the ramped cases from a written rule, rolls the set up and names the distance to the target as an amount, then adjusts and tests again. Use it when running `ref/rev/set-the-quotas`.
license: CC-BY-4.0
metadata:
  agent: quota-setter
  agent-version: "1"
---

# Draft and test a number per patch

## What it does

Drafts a number on every patch from the carrying model and the
attainment curve, tests each one against the capacity behind it and
against what that patch actually closed, works the ramped cases from a
written rule, rolls the set up and names the distance to the target as
an amount, then adjusts and tests again. A gap is never spread evenly.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Adjust and Test Again**
  - `ref/rev/set-the-quotas`, activity 12 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Draft a Quota per Territory**
  - `ref/rev/set-the-quotas`, activity 6 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Roll Up and Name the Gap**
  - `ref/rev/set-the-quotas`, activity 11 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Test Against Capacity**
  - `ref/rev/set-the-quotas`, activity 7 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Work the Ramp Cases**
  - `ref/rev/set-the-quotas`, activity 9 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)

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
