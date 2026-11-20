---
name: check-an-entry
description: Reads every account in an entry as open and allowed for manual entries, reads the period as still open, and checks that debits equal credits in each entity and each currency and that every amount equals the support or the schedule behind it. Use it when running `ref/fin/account-for-a-lease` and `ref/fin/post-a-manual-journal-entry`.
license: CC-BY-4.0
metadata:
  agent: ledger-accountant
  agent-version: "1"
---

# Check an entry

## What it does

Reads every account in an entry as open and allowed for manual entries,
reads the period as still open, and checks that debits equal credits in
each entity and each currency and that every amount equals the support
or the schedule behind it.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check That the Entry Balances**
  - `ref/fin/post-a-manual-journal-entry`, activity 5 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Check the Accounts and the Period**
  - `ref/fin/post-a-manual-journal-entry`, activity 4 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Check the Opening Entry**
  - `ref/fin/account-for-a-lease`, activity 10 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)

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
