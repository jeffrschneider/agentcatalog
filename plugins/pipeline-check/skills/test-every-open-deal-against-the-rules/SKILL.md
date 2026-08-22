---
name: test-every-open-deal-against-the-rules
description: Tests each open deal against the fields it has to carry, the close date it claims, the stage its evidence supports, the amount its own line items price, and the owner, territory and team it sits under. Use it when running `ref/rev/enforce-pipeline-hygiene`.
license: CC-BY-4.0
metadata:
  agent: pipeline-check
  agent-version: "1"
---

# Test every open deal against the rules

## What it does

Tests each open deal against the fields it has to carry, the close date
it claims, the stage its evidence supports, the amount its own line
items price, and the owner, territory and team it sits under. Each check
is one rule family run over the whole extract.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Check Owner, Territory and Team**
  - `ref/rev/enforce-pipeline-hygiene`, activity 9 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Check the Amount Against What Is Priced**
  - `ref/rev/enforce-pipeline-hygiene`, activity 8 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Check the Close Dates**
  - `ref/rev/enforce-pipeline-hygiene`, activity 6 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Check the Required Fields**
  - `ref/rev/enforce-pipeline-hygiene`, activity 5 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Check the Stage Against the Evidence**
  - `ref/rev/enforce-pipeline-hygiene`, activity 7 -
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
