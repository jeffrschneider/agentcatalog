---
name: record-what-was-received
description: Records each delivery the requester confirms against the order, confirms the receipt when an invoice is matched, lists what was received and not yet invoiced at each period end, and passes each capital purchase to the asset register. Use it when running `ref/fin/account-for-fixed-assets` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: purchasing-coordinator
  agent-version: "1"
---

# Record what was received

## What it does

Records each delivery the requester confirms against the order, confirms
the receipt when an invoice is matched, lists what was received and not
yet invoiced at each period end, and passes each capital purchase to the
asset register.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Confirm What Was Received**
  - `ref/fin/process-a-supplier-invoice`, activity 6 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **List What Was Received and Not Invoiced**
  - `ref/fin/book-the-period-end-accruals`, activity 3 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Record What Was Received**
  - `ref/fin/issue-a-purchase-order`, activity 14 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Take In the Capital Purchases**
  - `ref/fin/account-for-fixed-assets`, activity 2 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)

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
