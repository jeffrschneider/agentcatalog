---
name: match-the-records-against-the-books
description: Sets the spend the systems recorded against what the books say and clears the differences the buy's own records already explain, leaving only the ones that need an answer from outside. Use it when running `ref/mkt/marketing-performance-report`, `ref/mkt/paid-search-campaign` and `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Match the records against the books

## What it does

Sets the spend the systems recorded against what the books say and
clears the differences the buy's own records already explain, leaving
only the ones that need an answer from outside.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Clear the Explained Differences**
  - `ref/mkt/reconcile-media-spend`, activity 8 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Reconcile the Spend**
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
