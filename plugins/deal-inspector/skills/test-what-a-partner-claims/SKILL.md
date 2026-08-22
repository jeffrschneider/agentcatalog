---
name: test-what-a-partner-claims
description: Reads what a partner brought against the standard the partner process sets. Use it when running `ref/prt/register-a-deal` and `ref/prt/resolve-a-channel-conflict`.
license: CC-BY-4.0
metadata:
  agent: deal-inspector
  agent-version: "1"
---

# Test what a partner claims

## What it does

Reads what a partner brought against the standard the partner process
sets. Where two parties claim the same customer, it tests who actually
brought them, against the evidence each side registered and the date it
was registered.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Read What the Partner Brought**
  - `ref/prt/register-a-deal`, activity 7 -
    [Register a Deal](../../../../processes/partners/register-a-deal.md)
- **Test Who Brought the Customer**
  - `ref/prt/resolve-a-channel-conflict`, activity 7 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)

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
