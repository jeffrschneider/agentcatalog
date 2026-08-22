---
name: tell-every-function-what-it-has
description: Each function hears its number and the rules with it. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Tell Every Function What It Has

## What happens

Each function hears its number and the rules with it.

## Where it happens

- `ref/mkt/set-marketing-budget`, activity 14 -
  [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
