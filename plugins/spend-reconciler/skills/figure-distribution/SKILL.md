---
name: figure-distribution
description: Sends a settled figure to everyone who works from it, which means the books and the reports for a verified spend, and every agent working to an allocation when that allocation changes. Use it when running `ref/mkt/reallocate-media-spend` and `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: spend-reconciler
  agent-version: "1"
---

# Figure distribution

## What it does

Sends a settled figure to everyone who works from it, which means the
books and the reports for a verified spend, and every agent working to
an allocation when that allocation changes.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Release the Figures**
  - `ref/mkt/reconcile-media-spend`, activity 13 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Tell the Agents that Read the Plan**
  - `ref/mkt/reallocate-media-spend`, activity 13 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

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
