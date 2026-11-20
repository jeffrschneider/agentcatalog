---
name: take-in-the-statement
description: Takes in every transaction on every card for the statement period, checks the issuer's statement against them, and sends the checked balance to the payment run by its due date. Use it when running `ref/fin/reconcile-company-card-spend`.
license: CC-BY-4.0
metadata:
  agent: card-administrator
  agent-version: "1"
---

# Take in the statement

## What it does

Takes in every transaction on every card for the statement period,
checks the issuer's statement against them, and sends the checked
balance to the payment run by its due date.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Statement Against the Transactions**
  - `ref/fin/reconcile-company-card-spend`, activity 2 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)
- **Send the Statement for Payment**
  - `ref/fin/reconcile-company-card-spend`, activity 3 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)
- **Take In the Statement**
  - `ref/fin/reconcile-company-card-spend`, activity 1 -
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
