---
name: period-summary
description: Works out what was actually spent over a past period from the records and sets it beside what was committed or what another party recorded, so both sides end up with one figure they agree on. Use it when running `ref/mkt/co-marketing-campaign` and `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: spend-reconciler
  agent-version: "1"
---

# Period summary

## What it does

Works out what was actually spent over a past period from the records
and sets it beside what was committed or what another party recorded, so
both sides end up with one figure they agree on.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Joint Numbers**
  - `ref/mkt/co-marketing-campaign`, activity 15 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Read Last Year's Spend**
  - `ref/mkt/set-marketing-budget`, activity 2 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

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
