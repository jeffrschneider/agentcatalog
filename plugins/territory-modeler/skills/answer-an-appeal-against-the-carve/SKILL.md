---
name: answer-an-appeal-against-the-carve
description: Takes the approved carve, builds each seller the statement of what they hold, tests every appeal against what is written down rather than against who is asking, and applies what changed. Use it when running `ref/rev/publish-the-carve`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Answer an appeal against the carve

## What it does

Takes the approved carve, builds each seller the statement of what they
hold, tests every appeal against what is written down rather than
against who is asking, and applies what changed.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Apply What Changed**
  - `ref/rev/publish-the-carve`, activity 12 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Build a Statement per Seller**
  - `ref/rev/publish-the-carve`, activity 3 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Take in the Approved Carve**
  - `ref/rev/publish-the-carve`, activity 1 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Test Each Appeal Against the Record**
  - `ref/rev/publish-the-carve`, activity 10 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)

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
