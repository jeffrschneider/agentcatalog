---
name: set-what-a-close-or-an-audit-covers
description: Says which accounts, campaigns, channels and dates a close or an audit covers, before any records are pulled. Use it when running `ref/mkt/reconcile-media-spend` and `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Set what a close or an audit covers

## What it does

Says which accounts, campaigns, channels and dates a close or an audit
covers, before any records are pulled.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set What the Audit Covers**
  - `ref/mkt/verify-ad-placement`, activity 2 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Set What the Close Covers**
  - `ref/mkt/reconcile-media-spend`, activity 1 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
