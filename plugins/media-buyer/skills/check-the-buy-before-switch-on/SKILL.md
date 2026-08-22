---
name: check-the-buy-before-switch-on
description: The caps, pools and exclusions are as agreed. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Check the Buy Before Switch-On

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/display-retargeting`, the caps, pools and exclusions are
  as agreed
- in `ref/mkt/traffic-ad-creative`, every ad read against the plan line
  and the rules

## Where it happens

- `ref/mkt/display-retargeting`, activity 12 -
  [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- `ref/mkt/traffic-ad-creative`, activity 14 -
  [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
