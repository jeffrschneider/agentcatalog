---
name: gather-the-account
description: Takes in each account on the reconciliation list with its risk, its source, its due day and the items the last period carried forward, and pulls the closing balance and the period's entries from the ledger beside the source that backs it. Use it when running `ref/fin/reconcile-a-balance-sheet-account`.
license: CC-BY-4.0
metadata:
  agent: account-reconciler
  agent-version: "1"
---

# Gather the account

## What it does

Takes in each account on the reconciliation list with its risk, its
source, its due day and the items the last period carried forward, and
pulls the closing balance and the period's entries from the ledger
beside the source that backs it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Pull the Ledger Balance**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 2 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Pull the Source**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 3 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Take In the Account**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 1 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)

## What to record

Each reconciliation leaves the account with its risk, its source and its
due day, the open items the last period carried forward, the closing
balance and the period's entries, the source as it was pulled with its
date, each entry matched to its source item and each item left unmatched
on either side, each difference explained as timing, an error or a
missing entry with the evidence that shows which, each account owner's
answer, each clearing entry proposed with its support and as posted with
its approval, and each open item with its age, its owner and its date to
clear. Beside the sheet sit the controller's decision on each old or
large item, the preparer named, the reviewer's sign-off with its date,
and the sheet kept with its evidence for the audit. Each consolidation
leaves every pair of entities' balances and trading side by side in one
currency, each mismatch explained as timing, rate or error with the
evidence from both sides, and the corrections and settlements the entity
controllers agreed in writing. Nothing in the record shows this agent
signing off a reconciliation, posting an entry, or clearing a difference
with an entry whose only support is the difference itself.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
