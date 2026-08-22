---
name: pull-the-delivery-record
description: What each platform recorded as delivered and spent. Use it when running `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Pull the Delivery Record

## What happens

What each platform recorded as delivered and spent.

## Where it happens

- `ref/mkt/reconcile-media-spend`, activity 3 -
  [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
