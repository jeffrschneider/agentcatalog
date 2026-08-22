---
name: record-what-was-learned
description: Which lines and which issuers to check first next time. Use it when running `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: spend-reconciler
  agent-version: "1"
---

# Record What Was Learned

## What happens

Which lines and which issuers to check first next time.

## Where it happens

- `ref/mkt/reconcile-media-spend`, activity 14 -
  [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)

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
