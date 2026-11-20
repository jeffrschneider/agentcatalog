---
name: close-out-each-payment
description: Sends each payee its remittance advice, records the payments in the ledger, passes any part of a claim treated as pay to payroll before its cutoff, and confirms each employee's payment against the bank's report. Use it when running `ref/fin/pay-approved-invoices` and `ref/fin/reimburse-an-expense-claim`.
license: CC-BY-4.0
metadata:
  agent: payables-processor
  agent-version: "1"
---

# Close out each payment

## What it does

Sends each payee its remittance advice, records the payments in the
ledger, passes any part of a claim treated as pay to payroll before its
cutoff, and confirms each employee's payment against the bank's report.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Employee Was Paid**
  - `ref/fin/reimburse-an-expense-claim`, activity 11 -
    [Reimburse an Expense Claim](../../../../processes/finance/reimburse-an-expense-claim.md)
- **Pass the Part Treated as Pay to Payroll**
  - `ref/fin/reimburse-an-expense-claim`, activity 10 -
    [Reimburse an Expense Claim](../../../../processes/finance/reimburse-an-expense-claim.md)
- **Record the Payments in the Ledger**
  - `ref/fin/pay-approved-invoices`, activity 14 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)
- **Send the Remittance Advice**
  - `ref/fin/pay-approved-invoices`, activity 13 -
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
