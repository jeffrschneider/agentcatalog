---
name: keep-each-customers-account
description: Keeps each customer's account showing every open invoice, its age and anything held or in dispute, confirms that an overdue invoice is still owed, checks each promise to pay against the receipts, and records the outcome of each follow-up. Use it when running `ref/fin/apply-a-customer-payment` and `ref/fin/collect-an-overdue-invoice`.
license: CC-BY-4.0
metadata:
  agent: receivables-keeper
  agent-version: "1"
---

# Keep each customers account

## What it does

Keeps each customer's account showing every open invoice, its age and
anything held or in dispute, confirms that an overdue invoice is still
owed, checks each promise to pay against the receipts, and records the
outcome of each follow-up.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Check Each Promise Was Kept**
  - `ref/fin/collect-an-overdue-invoice`, activity 8 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Confirm the Invoice Is Still Owed**
  - `ref/fin/collect-an-overdue-invoice`, activity 2 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Record the Outcome**
  - `ref/fin/collect-an-overdue-invoice`, activity 15 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Take In the Overdue Invoice**
  - `ref/fin/collect-an-overdue-invoice`, activity 1 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Update Each Customer's Account**
  - `ref/fin/apply-a-customer-payment`, activity 13 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)

## What to record

Each day leaves every receipt on the bank's report with the remittance
kept beside it, the customer identified or the reason it could not be,
each match with the rule that made it, each receipt applied or held with
its reason, and the applied and held amounts agreed to the bank's total.
Each held receipt leaves the customer's answer, the named person's
decision and what was applied, kept on account or passed for refund, and
each customer's account shows every open invoice, its age and anything
held or in dispute. Each overdue invoice leaves the check that it was
still owed, each promise set against the receipts on its date, and the
outcome. Each write-off leaves the amount still owed on each invoice,
the security and other routes, the proposal as set out, the write-off
recorded for exactly the amount approved with the approval and its
version attached, the notice to tax and to the close, and any later
payment applied as a recovery. Nothing in the record shows this agent
clearing a shortfall, moving money between customers, refunding money or
writing off a debt on its own.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
