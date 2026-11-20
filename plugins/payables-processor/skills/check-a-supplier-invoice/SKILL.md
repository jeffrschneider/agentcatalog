---
name: check-a-supplier-invoice
description: Captures every field of an invoice, checks the supplier's record and bank details, looks for a duplicate, reads the invoice against the local invoice rules, finds its purchase order, matches it to the order and the receipt, and asks the supplier for a correction when it is wrong. Use it when running `ref/fin/process-a-supplier-invoice`.
license: CC-BY-4.0
metadata:
  agent: payables-processor
  agent-version: "1"
---

# Check a supplier invoice

## What it does

Captures every field of an invoice, checks the supplier's record and
bank details, looks for a duplicate, reads the invoice against the local
invoice rules, finds its purchase order, matches it to the order and the
receipt, and asks the supplier for a correction when it is wrong.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Ask the Supplier for a Correction**
  - `ref/fin/process-a-supplier-invoice`, activity 10 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Capture the Invoice**
  - `ref/fin/process-a-supplier-invoice`, activity 1 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Check What the Invoice Must Show**
  - `ref/fin/process-a-supplier-invoice`, activity 4 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Check for a Duplicate**
  - `ref/fin/process-a-supplier-invoice`, activity 3 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Check the Supplier Record**
  - `ref/fin/process-a-supplier-invoice`, activity 2 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Find the Purchase Order**
  - `ref/fin/process-a-supplier-invoice`, activity 5 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
- **Match the Invoice**
  - `ref/fin/process-a-supplier-invoice`, activity 7 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)

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
