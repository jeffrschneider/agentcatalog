---
name: correct-the-pacing
description: Daily limits reset so each flight lands on its date. Use it when running `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Correct the Pacing

## What happens

Daily limits reset so each flight lands on its date.

## Where it happens

- `ref/mkt/reallocate-media-spend`, activity 11 -
  [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
