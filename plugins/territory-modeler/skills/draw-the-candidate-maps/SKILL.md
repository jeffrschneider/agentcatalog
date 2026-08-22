---
name: draw-the-candidate-maps
description: Draws candidate cuts on that rule with every account placed exactly once, and fixes the one a named person chooses, carrying its version, the rule it was drawn on and the date it takes effect. Use it when running `ref/rev/model-the-territories`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Draw the candidate maps

## What it does

Draws candidate cuts on that rule with every account placed exactly
once, and fixes the one a named person chooses, carrying its version,
the rule it was drawn on and the date it takes effect. The maps that
lost are kept, each with the reason it lost.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Draw the Candidate Cuts**
  - `ref/rev/model-the-territories`, activity 7 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)
- **Fix the Territory Map**
  - `ref/rev/model-the-territories`, activity 13 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)

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
