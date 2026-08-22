---
name: close-a-lost-deal-out
description: Sets the date to come back and what would have to change by then, tells the people who worked the deal before they hear it somewhere else, closes the record, and feeds the loss into the review that reads them together. Use it when running `ref/sls/record-a-lost-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-inspector
  agent-version: "1"
---

# Close a lost deal out

## What it does

Sets the date to come back and what would have to change by then, tells
the people who worked the deal before they hear it somewhere else,
closes the record, and feeds the loss into the review that reads them
together.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Close the Record**
  - `ref/sls/record-a-lost-deal`, activity 13 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)
- **Feed the Loss into the Review**
  - `ref/sls/record-a-lost-deal`, activity 14 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)
- **Set the Follow-Up Date**
  - `ref/sls/record-a-lost-deal`, activity 11 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)
- **Tell the People Who Worked It**
  - `ref/sls/record-a-lost-deal`, activity 12 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

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
