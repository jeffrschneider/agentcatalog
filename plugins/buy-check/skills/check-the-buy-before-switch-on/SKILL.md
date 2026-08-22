---
name: check-the-buy-before-switch-on
description: The caps, pools and exclusions are as agreed. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: buy-check
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

A verdict per item, each citing the plan line or the rule, its version,
and the campaign configuration it was read against. A pre-launch score
and a post-delivery score, each dated and each naming what it read.
Anything it could not test is recorded as untested rather than left out.
A rescore after a fix names what changed and what it ran again. Where
what ran differs from what was ordered, the difference is recorded
against the plan line it belongs to, with the figures on both sides.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
