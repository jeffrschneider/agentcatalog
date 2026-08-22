---
name: apply-the-exclusions
description: Block lists and inventory settings are changed. Use it when running `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Apply the Exclusions

## What happens

Block lists and inventory settings are changed.

## Where it happens

- `ref/mkt/verify-ad-placement`, activity 10 -
  [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
