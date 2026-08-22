---
name: read-the-rules-at-a-version
description: Reads the field rules and the stage definitions as they are written, at a version, and gets a sales leader to settle how old a deal may get in a stage before it counts as stale. Use it when running `ref/rev/enforce-pipeline-hygiene`.
license: CC-BY-4.0
metadata:
  agent: pipeline-check
  agent-version: "1"
---

# Read the rules at a version

## What it does

Reads the field rules and the stage definitions as they are written, at
a version, and gets a sales leader to settle how old a deal may get in a
stage before it counts as stale. Nothing is checked against a rule that
is not written down somewhere.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Agree What Counts as Stale**
  - `ref/rev/enforce-pipeline-hygiene`, activity 3 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Read the Rules as Written**
  - `ref/rev/enforce-pipeline-hygiene`, activity 2 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)

## What to record

Per run: the rules and stage definitions at the version they were read
at, the extract every check ran against, and the staleness numbers with
who agreed them. Per finding: the deal, the rule it failed, the amount
it moves, the person it was sent to and the date it was sent. Withdrawn
findings are kept as withdrawn with the reason, and a dispute is kept
whether or not the finding stood, because a rule many owners dispute is
the next amendment. Every mark carried into the roll-up names its rule
and its date. Somebody auditing a run can replay each finding against
the extract behind it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
