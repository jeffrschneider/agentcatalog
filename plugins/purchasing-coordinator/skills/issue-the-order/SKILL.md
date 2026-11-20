---
name: issue-the-order
description: Builds the approved request into an order at a version with its terms, sends it to the supplier through the contact on its record before any work starts, and records the supplier's acceptance or the change it asks for. Use it when running `ref/fin/issue-a-purchase-order`.
license: CC-BY-4.0
metadata:
  agent: purchasing-coordinator
  agent-version: "1"
---

# Issue the order

## What it does

Builds the approved request into an order at a version with its terms,
sends it to the supplier through the contact on its record before any
work starts, and records the supplier's acceptance or the change it asks
for.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Issue the Order**
  - `ref/fin/issue-a-purchase-order`, activity 11 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Record the Supplier's Acceptance**
  - `ref/fin/issue-a-purchase-order`, activity 13 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Send the Order to the Supplier**
  - `ref/fin/issue-a-purchase-order`, activity 12 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)

## What to record

Each request leaves what was asked for with the requester, the amount,
the budget line and the dates, any field asked for again and when it
came, the supplier's record and, above the threshold, the choice behind
it, and any request held for a choice or a setup with the date it was
expected. Beside it sit the room the budget-keeper agent found, the
approvals the delegation-keeper agent counted and the commitment
recorded. Each order leaves its versions with their terms, the date it
was sent and the contact it went to, the supplier's acceptance or the
change it asked for, each receipt with who confirmed it, the quantity
and the date, anything damaged, short or late with the reason, and the
close with the amount released from the line. Work started or goods
delivered before an order was approved are recorded as an exception.
Each period leaves the list of what was received and not yet invoiced
and the capital purchases passed to the register. Nothing in the record
shows this agent approving a purchase, committing money or moving money
between budget lines.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
