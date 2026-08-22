---
name: move-an-account-between-patches
description: Takes in a request to move an account, finds the line of the carve that allows it, and records the move against the carve. Use it when running `ref/rev/move-an-account`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Move an account between patches

## What it does

Takes in a request to move an account, finds the line of the carve that
allows it, and records the move against the carve. An account the rule
is silent about goes to whoever amends the rule instead.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Find the Rule That Allows It**
  - `ref/rev/move-an-account`, activity 3 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Record the Move Against the Carve**
  - `ref/rev/move-an-account`, activity 14 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Take in the Request**
  - `ref/rev/move-an-account`, activity 1 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)

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
