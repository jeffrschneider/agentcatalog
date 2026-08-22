---
name: pull-the-record-of-what-actually-ran
description: "Pulls the record of what happened out of each system: what was ordered and at which rates, what was recorded as delivered and spent, and every site, app and channel the ads actually ran on. Use it when running `ref/mkt/reconcile-media-spend` and `ref/mkt/verify-ad-placement`."
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Pull the record of what actually ran

## What it does

Pulls the record of what happened out of each system: what was ordered
and at which rates, what was recorded as delivered and spent, and every
site, app and channel the ads actually ran on.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Pull the Delivery Record**
  - `ref/mkt/reconcile-media-spend`, activity 3 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Pull the Order Record**
  - `ref/mkt/reconcile-media-spend`, activity 4 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Pull the Placement Record**
  - `ref/mkt/verify-ad-placement`, activity 4 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
