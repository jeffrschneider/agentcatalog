---
name: hand-the-map-to-quota-setting
description: Hands the fixed map and its carrying numbers to whoever puts a number on each patch, and stands behind the map while that work runs. Use it when running `ref/rev/model-the-territories` and `ref/rev/set-the-quotas`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Hand the map to quota setting

## What it does

Hands the fixed map and its carrying numbers to whoever puts a number on
each patch, and stands behind the map while that work runs.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand the Map to Quota Setting**
  - `ref/rev/model-the-territories`, activity 15 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)
- **Take in the Map and the Number**
  - `ref/rev/set-the-quotas`, activity 1 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)

## What to record

Per run: the carve rule as it was agreed and the fields it reads, each
candidate map with every account placed exactly once, and a carrying
number per patch naming the data it was computed from. A number that
cannot name its source is marked unsourced where a reader sees it. The
maps that lost are kept, each with the reason it lost. The fixed map
carries its version, the rule it was drawn on and the date it takes
effect, and beside every carrying number sits the assumption it rests on
and what would make that assumption wrong. Anybody auditing a run can
redraw it from what is written down.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
