---
name: test-what-a-deal-rests-on
description: Names who signs and who can stop it, marking each person met or unmet, and looks for the customer's own words rather than the champion's. Use it when running `ref/sls/inspect-a-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-inspector
  agent-version: "1"
---

# Test what a deal rests on

## What it does

Names who signs and who can stop it, marking each person met or unmet,
and looks for the customer's own words rather than the champion's.
Checks the money exists and belongs to somebody, and reads who else is
in the deal and what would have to be true to win it.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Money Is Real**
  - `ref/sls/inspect-a-deal`, activity 6 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Name the Buying Group**
  - `ref/sls/inspect-a-deal`, activity 4 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Read the Competitive Position**
  - `ref/sls/inspect-a-deal`, activity 7 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Test What the Customer Said**
  - `ref/sls/inspect-a-deal`, activity 5 -
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
