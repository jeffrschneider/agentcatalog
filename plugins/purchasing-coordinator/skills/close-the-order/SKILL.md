---
name: close-the-order
description: Closes the order once it is received in full and its last invoice is matched, or once it is cancelled, has what is left released from the budget line, and records what the run taught. Use it when running `ref/fin/issue-a-purchase-order`.
license: CC-BY-4.0
metadata:
  agent: purchasing-coordinator
  agent-version: "1"
---

# Close the order

## What it does

Closes the order once it is received in full and its last invoice is
matched, or once it is cancelled, has what is left released from the
budget line, and records what the run taught.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Close the Order**
  - `ref/fin/issue-a-purchase-order`, activity 15 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Record What the Run Taught**
  - `ref/fin/issue-a-purchase-order`, activity 16 -
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
