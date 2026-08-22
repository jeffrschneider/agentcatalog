---
name: read-back-and-version-the-record
description: Reads the record back to the buyer for confirmation, versions it with the earlier versions still readable, and hands that one version to shaping. Use it when running `ref/sls/record-the-requirements`.
license: CC-BY-4.0
metadata:
  agent: requirements-recorder
  agent-version: "1"
---

# Read back and version the record

## What it does

Reads the record back to the buyer for confirmation, versions it with
the earlier versions still readable, and hands that one version to
shaping. The record does not go forward as confirmed on silence.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Hand the Record to Shaping**
  - `ref/sls/record-the-requirements`, activity 12 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Read the Record Back**
  - `ref/sls/record-the-requirements`, activity 10 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Version the Record**
  - `ref/sls/record-the-requirements`, activity 11 -
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
