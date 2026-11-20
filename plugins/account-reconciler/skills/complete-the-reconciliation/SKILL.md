---
name: complete-the-reconciliation
description: Ages every item still open against the ageing rule, raises an old or large item with the controller, puts the balance, the source, the items and the explanations on one sheet at a version for the named reviewer, and keeps the signed sheet with its evidence for the audit. Use it when running `ref/fin/close-the-month` and `ref/fin/reconcile-a-balance-sheet-account`.
license: CC-BY-4.0
metadata:
  agent: account-reconciler
  agent-version: "1"
---

# Complete the reconciliation

## What it does

Ages every item still open against the ageing rule, raises an old or
large item with the controller, puts the balance, the source, the items
and the explanations on one sheet at a version for the named reviewer,
and keeps the signed sheet with its evidence for the audit.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Age the Open Items**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 10 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Complete the Reconciliation**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 12 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Keep the Reconciliation**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 14 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Raise an Old or Large Item**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 11 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Reconcile the Accounts**
  - `ref/fin/close-the-month`, activity 6 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Record What the Reconciliation Taught**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 15 -
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
