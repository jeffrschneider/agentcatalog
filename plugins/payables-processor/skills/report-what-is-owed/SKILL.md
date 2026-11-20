---
name: report-what-is-owed
description: Gives the cash forecast each approved invoice and open order by the week it falls due, and the daily cash position the payments due out that day with the approval behind each. Use it when running `ref/fin/forecast-cash` and `ref/fin/report-the-daily-cash-position`.
license: CC-BY-4.0
metadata:
  agent: payables-processor
  agent-version: "1"
---

# Report what is owed

## What it does

Gives the cash forecast each approved invoice and open order by the week
it falls due, and the daily cash position the payments due out that day
with the approval behind each.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Gather What the Company Owes**
  - `ref/fin/forecast-cash`, activity 3 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **List the Payments Due Today**
  - `ref/fin/report-the-daily-cash-position`, activity 5 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)

## What to record

Each invoice leaves every field as captured beside the image, the
supplier record and the bank details it was checked against, the
duplicate check, the reading against the local invoice rules, the order
and the receipt it was matched to with each difference, any exception
with the approver's decision, any correction asked of the supplier, the
coding, the due date with the approval behind it, the posting and where
the invoice is kept. Each payment run leaves its date and its paying
account, every item gathered, every item held with its reason and the
person told, the run at the version the approver approved, the payment
file with each payment traced to an approved item and a verified record,
the release by two named people, the remittance advice sent, and the
ledger agreed to the approved run. Each claim leaves its coding, the run
it was proposed in, any part passed to payroll with the approval behind
it, the payment as the bank reported it, and its receipts kept. Nothing
in the record shows this agent approving an exception or a run,
releasing money, or changing an amount a supplier billed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
