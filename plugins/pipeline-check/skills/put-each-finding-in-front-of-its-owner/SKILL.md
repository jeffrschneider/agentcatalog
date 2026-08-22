---
name: put-each-finding-in-front-of-its-owner
description: Orders the findings by the amount each one moves, then sends each one to the person who owns that deal, naming the rule it failed and the money behind it. Use it when running `ref/rev/enforce-pipeline-hygiene`.
license: CC-BY-4.0
metadata:
  agent: pipeline-check
  agent-version: "1"
---

# Put each finding in front of its owner

## What it does

Orders the findings by the amount each one moves, then sends each one to
the person who owns that deal, naming the rule it failed and the money
behind it. A finding lands on a person, not in a report nobody acts on.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Rank the Findings by What They Move**
  - `ref/rev/enforce-pipeline-hygiene`, activity 11 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Send Each Finding to the Deal's Owner**
  - `ref/rev/enforce-pipeline-hygiene`, activity 12 -
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
