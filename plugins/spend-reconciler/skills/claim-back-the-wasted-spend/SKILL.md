---
name: claim-back-the-wasted-spend
description: The failed impressions go back to whoever billed them. Use it when running `ref/mkt/verify-ad-placement`.
license: CC-BY-4.0
metadata:
  agent: spend-reconciler
  agent-version: "1"
---

# Claim Back the Wasted Spend

## What happens

The failed impressions go back to whoever billed them.

## Where it happens

- `ref/mkt/verify-ad-placement`, activity 12 -
  [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)

## What to record

The reconciliation for the period at a version, one row per line: what
was ordered, what ran, what was billed, the difference, and the amount
at stake. Against every unmatched line, the question that went to the
issuer, the date it went, the answer that came back, and what that
answer settled. A line still open on the day the period closes is
recorded as open, with its age and its amount. A credit is recorded
against the line it settles, so the next period is checked against a
figure that already accounts for it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
