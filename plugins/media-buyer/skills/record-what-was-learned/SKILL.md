---
name: record-what-was-learned
description: Which lines and which issuers to check first next time. Use it when running `ref/mkt/reconcile-media-spend` and `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Record What Was Learned

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/reconcile-media-spend`, which lines and which issuers to
  check first next time
- in `ref/mkt/verify-ad-placement`, which channels and sellers to check
  first next time

## Where it happens

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
