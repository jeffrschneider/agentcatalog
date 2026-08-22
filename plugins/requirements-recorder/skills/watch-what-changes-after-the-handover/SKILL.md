---
name: watch-what-changes-after-the-handover
description: Watches for the requirements that arrive after confirmation, and versions each one in rather than absorbing it quietly. Use it when running `ref/sls/record-the-requirements`, `ref/sls/run-a-proof-of-value` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: requirements-recorder
  agent-version: "1"
---

# Watch what changes after the handover

## What it does

Watches for the requirements that arrive after confirmation, and
versions each one in rather than absorbing it quietly. Reads the shape
back against the record line by line, showing each requirement met,
deferred or refused, and records what a trial and the run itself taught.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Map the Shape to the Requirements**
  - `ref/sls/shape-the-solution`, activity 10 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Record What Was Learned**
  - `ref/sls/record-the-requirements`, activity 14 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Record the Result and What It Taught**
  - `ref/sls/run-a-proof-of-value`, activity 15 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Watch for Drift While Shaping**
  - `ref/sls/record-the-requirements`, activity 13 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)

## What to record

One line per requirement, quoted in the buyer's words, with any
paraphrase marked as a paraphrase, the person who asked for it, and the
date they asked. The needs-and-wants split, with who drew the line. The
contradictions found, and what came back when each went to the buyer.
The buyer's ranking, recorded as the buyer's, with any seller re-ranking
kept beside it as a separate marked opinion. The requirements marked as
unmeetable, each with its reason and the date it was marked. The
read-back and the buyer's confirmation. The version number and its date,
with earlier versions still readable, and every later requirement
written, attributed and versioned in rather than absorbed quietly. The
mapping of shape to record, showing each requirement met, deferred or
refused.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
