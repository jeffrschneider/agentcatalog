---
name: chase-receipts-and-reasons
description: Tells each holder which transactions still need a receipt, a reason or a cost center, chases each missing one on a schedule and then with the holder's manager, and keeps personal spend open until it is repaid. Use it when running `ref/fin/reconcile-company-card-spend`.
license: CC-BY-4.0
metadata:
  agent: card-administrator
  agent-version: "1"
---

# Chase receipts and reasons

## What it does

Tells each holder which transactions still need a receipt, a reason or a
cost center, chases each missing one on a schedule and then with the
holder's manager, and keeps personal spend open until it is repaid.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Ask Each Holder for Receipts and Reasons**
  - `ref/fin/reconcile-company-card-spend`, activity 4 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)
- **Chase the Missing Receipts**
  - `ref/fin/reconcile-company-card-spend`, activity 7 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)
- **Recover Personal Spend**
  - `ref/fin/reconcile-company-card-spend`, activity 10 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)

## What to record

Each card request leaves the request with its reason, the reading
against the card policy, the approver the delegation-keeper agent named,
the limit and the rules that person set in writing, the holder's
acceptance of the terms at their versions, the order to the issuer, the
activation date, and the card in the portal matched field by field to
the register. Each freeze, close or change leaves the breach, the last
day or the approval behind it, the time it took effect and the people
told, and any spend handed to the reconciliation. Each statement period
leaves every transaction taken in, the statement checked against them,
the balance sent for payment, each request and reminder for a receipt,
each transaction's result from the expense-check agent with its approval
or decision, the personal spend and when it was repaid, and the
reconciliation with each difference explained by its evidence, its
proposed entry and the reviewer's sign-off. Nothing in the record shows
this agent setting a limit nobody approved, paying a card bill or
signing off a reconciliation it prepared.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
