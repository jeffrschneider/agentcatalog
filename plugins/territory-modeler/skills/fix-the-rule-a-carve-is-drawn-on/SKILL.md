---
name: fix-the-rule-a-carve-is-drawn-on
description: Takes in how many territories are wanted and the shape they should have, and fixes what a territory is cut on before anything is drawn. Use it when running `ref/rev/model-the-territories`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Fix the rule a carve is drawn on

## What it does

Takes in how many territories are wanted and the shape they should have,
and fixes what a territory is cut on before anything is drawn. A rule
changed after the maps exist voids them, and the draw runs again.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Fix What a Territory Is Cut On**
  - `ref/rev/model-the-territories`, activity 2 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)
- **Take in the Number and the Shape**
  - `ref/rev/model-the-territories`, activity 1 -
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
