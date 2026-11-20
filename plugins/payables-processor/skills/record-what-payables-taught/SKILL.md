---
name: record-what-payables-taught
description: Records the cause of each invoice exception, the items held from each run, the payments returned and the discounts missed, and what the next invoice or run does differently. Use it when running `ref/fin/pay-approved-invoices` and `ref/fin/process-a-supplier-invoice`.
license: CC-BY-4.0
metadata:
  agent: payables-processor
  agent-version: "1"
---

# Record what payables taught

## What it does

Records the cause of each invoice exception, the items held from each
run, the payments returned and the discounts missed, and what the next
invoice or run does differently.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What the Invoice Taught**
  - `ref/fin/process-a-supplier-invoice`, activity 15 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Record What the Run Taught**
  - `ref/fin/pay-approved-invoices`, activity 16 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)

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
