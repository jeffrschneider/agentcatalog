# account-reconciler

## gather-the-account

Takes in each account on the reconciliation list with its risk, its
source, its due day and the items the last period carried forward, and
pulls the closing balance and the period's entries from the ledger
beside the source that backs it.

covers:
- Pull the Ledger Balance
- Pull the Source
- Take In the Account

## match-and-explain-differences

Matches each ledger entry to its source item by amount, date and
reference, explains each unmatched item as timing, an error or a missing
entry with its evidence, asks the account owner about anything the
evidence does not explain, and proposes the entry that clears each
error.

covers:
- Ask the Account Owner
- Explain Each Difference
- Match the Entries to the Source
- Propose the Clearing Entries

## complete-the-reconciliation

Ages every item still open against the ageing rule, raises an old or
large item with the controller, puts the balance, the source, the items
and the explanations on one sheet at a version for the named reviewer,
and keeps the signed sheet with its evidence for the audit.

covers:
- Age the Open Items
- Complete the Reconciliation
- Keep the Reconciliation
- Raise an Old or Large Item
- Reconcile the Accounts
- Record What the Reconciliation Taught

## match-balances-between-entities

Sets each pair of entities' balances and trading with each other side
by side in one currency across the whole group, explains each mismatch
as timing, rate or error with the evidence from both sides, and sets out
the corrections and settlements for the two entity controllers to agree.

covers:
- Agree the Corrections and Settlements
- Explain Each Mismatch
- Match the Balances Between Entities
- Record What the Consolidation Taught
