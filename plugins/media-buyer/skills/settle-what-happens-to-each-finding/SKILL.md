---
name: settle-what-happens-to-each-finding
description: Decides what to do with each thing a close or an audit turned up, whether to exclude it, contest it or accept it and say why, claims back what was spent on impressions that failed, and follows every query through to a credit, a fix, a make-good or a refusal. Use it when running `ref/mkt/reconcile-media-spend` and `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Settle what happens to each finding

## What it does

Decides what to do with each thing a close or an audit turned up,
whether to exclude it, contest it or accept it and say why, claims back
what was spent on impressions that failed, and follows every query
through to a credit, a fix, a make-good or a refusal.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Claim Back the Wasted Spend**
  - `ref/mkt/verify-ad-placement`, activity 12 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Decide What Happens to Each**
  - `ref/mkt/verify-ad-placement`, activity 9 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Track the Answers**
  - `ref/mkt/reconcile-media-spend`, activity 10 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
