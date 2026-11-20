---
name: book-the-accruals
description: Opens each period's accruals, reverses the ones the last period marked to reverse, works out the pay owed, the prepaid costs to spread and the price of each cost received and not yet invoiced, sets each accrual beside the last period and the invoices since, prepares and posts the approved accrual journals with their reversal dates, and hands the schedule to the close. Use it when running `ref/fin/book-the-period-end-accruals` and `ref/fin/close-the-month`.
license: CC-BY-4.0
metadata:
  agent: ledger-accountant
  agent-version: "1"
---

# Book the accruals

## What it does

Opens each period's accruals, reverses the ones the last period marked
to reverse, works out the pay owed, the prepaid costs to spread and the
price of each cost received and not yet invoiced, sets each accrual
beside the last period and the invoices since, prepares and posts the
approved accrual journals with their reversal dates, and hands the
schedule to the close.

## Where it happens

The agent does this in twelve activities across two reference processes.
Each one names the activity as that process words it.

- **Book the Accruals**
  - `ref/fin/close-the-month`, activity 4 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Check Each Accrual Against the Last Period**
  - `ref/fin/book-the-period-end-accruals`, activity 9 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Confirm Costs With No Order**
  - `ref/fin/book-the-period-end-accruals`, activity 4 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Hand the Schedule to the Close**
  - `ref/fin/book-the-period-end-accruals`, activity 14 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Open the Period's Accruals**
  - `ref/fin/book-the-period-end-accruals`, activity 1 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Post the Accruals**
  - `ref/fin/book-the-period-end-accruals`, activity 13 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Prepare the Accrual Journals**
  - `ref/fin/book-the-period-end-accruals`, activity 10 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Price the Cost Accruals**
  - `ref/fin/book-the-period-end-accruals`, activity 8 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Record What the Period Taught**
  - `ref/fin/book-the-period-end-accruals`, activity 15 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Reverse the Last Period's Accruals**
  - `ref/fin/book-the-period-end-accruals`, activity 2 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Work Out the Pay Owed**
  - `ref/fin/book-the-period-end-accruals`, activity 6 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)
- **Work Out the Prepaid Costs to Spread**
  - `ref/fin/book-the-period-end-accruals`, activity 7 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)

## What to record

Each manual entry leaves the request with its reason and the person who
asked, the support behind each line, the entry as prepared with each
line's account, amount, entity, currency and description, the checks of
its accounts, its period and its balance, the approvers the delegation
named and each approval with its date, the posting and the read-back
that shows it posted once and equal to what was approved, any reversal
with its date, and any correction as a reversal and a new entry with the
approval behind each. Each period's accruals leave the accruals reversed
from the last period, the costs received and not yet invoiced, each
budget owner's confirmation or the mark that a cost was accrued without
one, the pay owed with the register behind it, the prepaid costs spread,
the commission taken in with any part marked incomplete, each accrual
set beside the last period with the cause of each one out of line, the
journals with their support and reversal dates, the reviewer's and any
senior approver's approval, the posting, and the schedule handed to the
close. Nothing in the record shows this agent approving an entry,
posting one before its approval, or editing a posted entry in place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
