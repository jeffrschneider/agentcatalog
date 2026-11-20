---
name: post-and-keep-entries
description: Posts each entry only once the named approvers who did not prepare it have approved it, whether a manual entry, a close journal, a clearing entry, a correcting entry or a lease opening entry, reads the posting back, schedules any reversal, corrects a wrong posting by reversing it, and files the entry with its support and its approvals. Use it when running `ref/fin/account-for-a-lease` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: ledger-accountant
  agent-version: "1"
---

# Post and keep entries

## What it does

Posts each entry only once the named approvers who did not prepare it
have approved it, whether a manual entry, a close journal, a clearing
entry, a correcting entry or a lease opening entry, reads the posting
back, schedules any reversal, corrects a wrong posting by reversing it,
and files the entry with its support and its approvals.

## Where it happens

The agent does this in ten activities across four reference processes.
Each one names the activity as that process words it.

- **Correct What the Check Found**
  - `ref/fin/close-the-month`, activity 10 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Correct a Posted Entry**
  - `ref/fin/post-a-manual-journal-entry`, activity 13 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **File the Entry**
  - `ref/fin/post-a-manual-journal-entry`, activity 14 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Post the Clearing Entries**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 9 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Post the Close Journals**
  - `ref/fin/close-the-month`, activity 5 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Post the Entry**
  - `ref/fin/post-a-manual-journal-entry`, activity 10 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Post the Opening Entry**
  - `ref/fin/account-for-a-lease`, activity 12 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)
- **Read the Posting Back**
  - `ref/fin/post-a-manual-journal-entry`, activity 11 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Record What the Entry Taught**
  - `ref/fin/post-a-manual-journal-entry`, activity 15 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Schedule the Reversal**
  - `ref/fin/post-a-manual-journal-entry`, activity 12 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)

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
