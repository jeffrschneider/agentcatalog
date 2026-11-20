---
name: record-what-receivables-taught
description: Records which receipts failed to match and why, what each customer should send next time, and which warning signs came before a debt was written off. Use it when running `ref/fin/apply-a-customer-payment` and `ref/fin/write-off-a-bad-debt`.
license: CC-BY-4.0
metadata:
  agent: receivables-keeper
  agent-version: "1"
---

# Record what receivables taught

## What it does

Records which receipts failed to match and why, what each customer
should send next time, and which warning signs came before a debt was
written off.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What the Debt Taught**
  - `ref/fin/write-off-a-bad-debt`, activity 16 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)
- **Record What the Run Taught**
  - `ref/fin/apply-a-customer-payment`, activity 15 -
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
