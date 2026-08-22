---
name: take-in-a-deal-and-pull-its-record
description: "Takes a deal in and pulls its own history: the stage, the amount and the close date as they stand, with every change and who made it. Use it when running `ref/sls/inspect-a-deal`."
license: CC-BY-4.0
metadata:
  agent: deal-inspector
  agent-version: "1"
---

# Take in a deal and pull its record

## What it does

Takes a deal in and pulls its own history: the stage, the amount and the
close date as they stand, with every change and who made it. The record
is where the inspection starts, not the seller's account of it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Pull the Deal Record**
  - `ref/sls/inspect-a-deal`, activity 2 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Take in the Deal**
  - `ref/sls/inspect-a-deal`, activity 1 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)

## What to record

Per inspection: the deal record with every change to stage, amount and
date carrying its author. The buying group, each named person marked met
or unmet. What the customer said, dated and quoted, and every place the
record holds nothing. The budget, the approver, and whether the money is
committed elsewhere. Who else is in it and what would have to be true to
win. Every remaining step with its owner and the time it takes, and
whether they fit before the close date or by how much they miss. Every
claim marked evidenced, asserted or absent, with the record and the date
behind each evidenced one. The one or two things that decide the deal.
The owner's answers as given, the actions with owners and dates, and the
category with who set it and their reason. Per loss: the signal, who
confirmed the decision, the loss date, the buyer's own words kept beside
one reason code, the winner or the decision to do nothing, any
contradiction between the stated reason and the record, and the
follow-up date with what would have to change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
