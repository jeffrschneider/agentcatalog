---
name: mark-the-claims-and-put-them-to-the-owner
description: Marks every claim evidenced, asserted or absent, names the one or two things that actually decide the deal, and puts the gaps to the owner to answer out loud. Use it when running `ref/sls/inspect-a-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-inspector
  agent-version: "1"
---

# Mark the claims and put them to the owner

## What it does

Marks every claim evidenced, asserted or absent, names the one or two
things that actually decide the deal, and puts the gaps to the owner to
answer out loud. Records where the deal stands with the person who said
so and the reason they gave.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Mark Each Claim**
  - `ref/sls/inspect-a-deal`, activity 10 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Name What the Deal Rests On**
  - `ref/sls/inspect-a-deal`, activity 11 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Put the Findings to the Owner**
  - `ref/sls/inspect-a-deal`, activity 12 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Record the Inspection**
  - `ref/sls/inspect-a-deal`, activity 15 -
    [Inspect a Deal](../../../../processes/sales/inspect-a-deal.md)
- **Say Where the Deal Stands**
  - `ref/sls/inspect-a-deal`, activity 14 -
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
