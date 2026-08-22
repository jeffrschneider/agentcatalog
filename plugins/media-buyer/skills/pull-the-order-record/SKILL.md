---
name: pull-the-order-record
description: What was ordered, at the rates that were agreed. Use it when running `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Pull the Order Record

## What happens

What was ordered, at the rates that were agreed.

## Where it happens

- `ref/mkt/reconcile-media-spend`, activity 4 -
  [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
