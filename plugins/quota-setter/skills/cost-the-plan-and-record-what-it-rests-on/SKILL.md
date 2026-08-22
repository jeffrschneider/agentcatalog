---
name: cost-the-plan-and-record-what-it-rests-on
description: Works out what the plan pays at the modelled, the target and the high case, and writes the curve, the history and the assumptions behind every number where the next round can read them. Use it when running `ref/rev/set-the-quotas`.
license: CC-BY-4.0
metadata:
  agent: quota-setter
  agent-version: "1"
---

# Cost the plan and record what it rests on

## What it does

Works out what the plan pays at the modelled, the target and the high
case, and writes the curve, the history and the assumptions behind every
number where the next round can read them.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Cost the Plan with Finance**
  - `ref/rev/set-the-quotas`, activity 13 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Record What the Quotas Rest On**
  - `ref/rev/set-the-quotas`, activity 15 -
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
