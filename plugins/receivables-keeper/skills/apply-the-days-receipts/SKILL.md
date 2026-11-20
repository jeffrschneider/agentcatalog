---
name: apply-the-days-receipts
description: Takes in each receipt on the bank's report with its remittance, identifies the customer that paid, matches each receipt to its invoices, applies the matched ones, holds aside anything short, over or unidentified, and agrees the day to the bank's total. Use it when running `ref/fin/apply-a-customer-payment`.
license: CC-BY-4.0
metadata:
  agent: receivables-keeper
  agent-version: "1"
---

# Apply the days receipts

## What it does

Takes in each receipt on the bank's report with its remittance,
identifies the customer that paid, matches each receipt to its invoices,
applies the matched ones, holds aside anything short, over or
unidentified, and agrees the day to the bank's total.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Account for Every Receipt**
  - `ref/fin/apply-a-customer-payment`, activity 7 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Apply the Matched Receipts**
  - `ref/fin/apply-a-customer-payment`, activity 5 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Gather the Remittance Advice**
  - `ref/fin/apply-a-customer-payment`, activity 2 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Hold Aside What Does Not Match**
  - `ref/fin/apply-a-customer-payment`, activity 6 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Identify the Customer That Paid**
  - `ref/fin/apply-a-customer-payment`, activity 3 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Match Each Receipt to Its Invoices**
  - `ref/fin/apply-a-customer-payment`, activity 4 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Take In the Day's Receipts**
  - `ref/fin/apply-a-customer-payment`, activity 1 -
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
