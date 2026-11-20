---
name: check-the-supplier
description: Checks that the supplier has an approved record and, above the threshold, a choice behind it or an agreement in force, sends the request to a choice of supplier or to supplier setup when either is missing, and hands the chosen supplier on. Use it when running `ref/fin/choose-a-supplier` and `ref/fin/issue-a-purchase-order`.
license: CC-BY-4.0
metadata:
  agent: purchasing-coordinator
  agent-version: "1"
---

# Check the supplier

## What it does

Checks that the supplier has an approved record and, above the
threshold, a choice behind it or an agreement in force, sends the
request to a choice of supplier or to supplier setup when either is
missing, and hands the chosen supplier on.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Ask for a Choice of Supplier**
  - `ref/fin/issue-a-purchase-order`, activity 5 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Ask for a New Supplier**
  - `ref/fin/issue-a-purchase-order`, activity 6 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Check for a Supplier Already Chosen**
  - `ref/fin/choose-a-supplier`, activity 2 -
    [Choose a Supplier](../../../../processes/finance/choose-a-supplier.md)
- **Check the Supplier**
  - `ref/fin/issue-a-purchase-order`, activity 4 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Hand the Supplier On**
  - `ref/fin/choose-a-supplier`, activity 16 -
    [Choose a Supplier](../../../../processes/finance/choose-a-supplier.md)

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
