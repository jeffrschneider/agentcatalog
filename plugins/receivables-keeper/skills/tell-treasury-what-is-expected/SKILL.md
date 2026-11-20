---
name: tell-treasury-what-is-expected
description: Gives the treasury-analyst agent what customers owe with the week each payment is expected, the receipts expected each day and each payment a remittance announced, and matches each day's bank movements to them. Use it when running `ref/fin/apply-a-customer-payment`, `ref/fin/forecast-cash` and `ref/fin/report-the-daily-cash-position`.
license: CC-BY-4.0
metadata:
  agent: receivables-keeper
  agent-version: "1"
---

# Tell treasury what is expected

## What it does

Gives the treasury-analyst agent what customers owe with the week each
payment is expected, the receipts expected each day and each payment a
remittance announced, and matches each day's bank movements to them.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Gather What Customers Owe**
  - `ref/fin/forecast-cash`, activity 2 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **List the Receipts Expected Today**
  - `ref/fin/report-the-daily-cash-position`, activity 4 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Match Each Movement to What Was Expected**
  - `ref/fin/report-the-daily-cash-position`, activity 6 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Tell Treasury What Is Expected**
  - `ref/fin/apply-a-customer-payment`, activity 14 -
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
