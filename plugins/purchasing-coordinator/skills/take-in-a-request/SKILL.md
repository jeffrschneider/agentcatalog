---
name: take-in-a-request
description: Takes in a request to buy or a purchase that needs a supplier chosen, and checks the request for a description, a quantity, a price basis, a budget line and the dates, asking the requester once for everything missing. Use it when running `ref/fin/choose-a-supplier` and `ref/fin/issue-a-purchase-order`.
license: CC-BY-4.0
metadata:
  agent: purchasing-coordinator
  agent-version: "1"
---

# Take in a request

## What it does

Takes in a request to buy or a purchase that needs a supplier chosen,
and checks the request for a description, a quantity, a price basis, a
budget line and the dates, asking the requester once for everything
missing.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Request Is Complete**
  - `ref/fin/issue-a-purchase-order`, activity 2 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Take in the Purchase**
  - `ref/fin/choose-a-supplier`, activity 1 -
    [Choose a Supplier](../../../../processes/finance/choose-a-supplier.md)
- **Take in the Request**
  - `ref/fin/issue-a-purchase-order`, activity 1 -
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
