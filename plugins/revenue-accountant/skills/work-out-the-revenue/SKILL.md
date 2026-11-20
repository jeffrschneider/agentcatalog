---
name: work-out-the-revenue
description: Asks each delivery owner to confirm what was delivered, works out each agreement's revenue for the period from its schedule, the delivery and the billing, and sends the revenue, deferred and unbilled entries with the schedule as their support to be approved and posted. Use it when running `ref/fin/recognize-revenue`.
license: CC-BY-4.0
metadata:
  agent: revenue-accountant
  agent-version: "1"
---

# Work out the revenue

## What it does

Asks each delivery owner to confirm what was delivered, works out each
agreement's revenue for the period from its schedule, the delivery and
the billing, and sends the revenue, deferred and unbilled entries with
the schedule as their support to be approved and posted.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Confirm What Was Delivered**
  - `ref/fin/recognize-revenue`, activity 8 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)
- **Send the Entries for Posting**
  - `ref/fin/recognize-revenue`, activity 10 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)
- **Work Out the Period's Revenue**
  - `ref/fin/recognize-revenue`, activity 9 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)

## What to record

Each period leaves its dates, its entity and the schedule as it stood at
the last close, each new or changed agreement read for each thing
promised, its price, its variable parts and when each is delivered, each
judgment set out with its options and their effect beside the decision
in writing with the reason and the person who made it, and each
agreement's schedule at a version naming the decision behind each line.
Beside the schedule sit what each delivery owner confirmed with the
record that shows it, what was billed, each agreement's revenue for the
period with the deferred and unbilled amounts that follow, the entries
sent for posting with the approval and the posting behind them, and the
reconciliation of the deferred and the unbilled revenue with every
difference explained. The run closes with the revenue accounting lead's
review and the handover to the close. Nothing in the record shows this
agent deciding a judgment, posting an entry, or working out revenue from
a term nobody booked.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
