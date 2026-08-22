---
name: take-in-the-discovery-notes
description: Takes the confirmed discovery notes in as the one source the record is written from, so what goes down is what the buyer said and not what was hoped for. Use it when running `ref/sls/record-the-requirements` and `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: requirements-recorder
  agent-version: "1"
---

# Take in the discovery notes

## What it does

Takes the confirmed discovery notes in as the one source the record is
written from, so what goes down is what the buyer said and not what was
hoped for.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand the Notes On**
  - `ref/sls/run-a-discovery-call`, activity 13 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Take in the Discovery Notes**
  - `ref/sls/record-the-requirements`, activity 1 -
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
