---
name: read-back-what-is-set-against-what-was-agreed
description: Reads what is actually set in the systems and compares it with what was decided, covering caps, pools, exclusions, splits, tags, variants and budgets, then reports anything that does not match. Use it when running `ref/mkt/display-retargeting` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Read back what is set against what was agreed

## What it does

Reads what is actually set in the systems and compares it with what was
decided, covering caps, pools, exclusions, splits, tags, variants and
budgets, then reports anything that does not match.

## Where it happens

The agent does this in three activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Buy Before Switch-On**
  - `ref/mkt/display-retargeting`, activity 12 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
  - `ref/mkt/traffic-ad-creative`, activity 14 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Check the Change Took**
  - `ref/mkt/reallocate-media-spend`, activity 12 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)
- **Check the Test Before Switch-On**
  - `ref/mkt/test-ad-creative`, activity 12 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
