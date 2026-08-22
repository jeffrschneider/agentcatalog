---
name: reconcile-the-spend
description: The spend figures checked against the books. Use it when running `ref/mkt/marketing-performance-report` and `ref/mkt/paid-search-campaign`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Reconcile the Spend

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/marketing-performance-report`, the spend figures checked
  against the books
- in `ref/mkt/paid-search-campaign`, the invoice matches what the run
  recorded

## Where it happens

- `ref/mkt/marketing-performance-report`, activity 10 -
  [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- `ref/mkt/paid-search-campaign`, activity 11 -
  [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
