---
name: set-up-a-path-for-leads-to-arrive
description: "Sets up the way leads reach the record: the capture fields and the scan or form behind them, and the partner records, tiers and registrations that incoming leads land against. Use it when running `ref/mkt/channel-program` and `ref/mkt/trade-show`."
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Set up a path for leads to arrive

## What it does

Sets up the way leads reach the record: the capture fields and the scan
or form behind them, and the partner records, tiers and registrations
that incoming leads land against.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set up Lead Capture**
  - `ref/mkt/trade-show`, activity 9 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Set up the Partner Systems**
  - `ref/mkt/channel-program`, activity 9 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
