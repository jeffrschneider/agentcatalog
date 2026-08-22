---
name: record-what-was-learned
description: Closes a run with what to check first the next time, naming the lines and the issuers that caused the most work. Use it when running `ref/mkt/reconcile-media-spend` and `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Record what was learned

## What it does

Closes a run with what to check first the next time, naming the lines
and the issuers that caused the most work.

## Where it happens

The agent does this in one activity across two reference processes. Each
one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/mkt/reconcile-media-spend`, activity 14 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
  - `ref/mkt/verify-ad-placement`, activity 15 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
