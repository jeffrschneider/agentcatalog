---
name: pay-and-file
description: Builds the payment file from the approved register to each employee's verified account, issues the payslips on payday, pays and files the withholding by its date, posts the period's journal to the ledger, and records what the run taught. Use it when running `ref/hr/run-payroll`.
license: CC-BY-4.0
metadata:
  agent: payroll-administrator
  agent-version: "1"
---

# Pay and file

## What it does

Builds the payment file from the approved register to each employee's
verified account, issues the payslips on payday, pays and files the
withholding by its date, posts the period's journal to the ledger, and
records what the run taught.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Build the Payment File**
  - `ref/hr/run-payroll`, activity 9 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Issue the Payslips**
  - `ref/hr/run-payroll`, activity 13 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Pay and File the Withholding**
  - `ref/hr/run-payroll`, activity 14 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Post the Payroll to the Ledger**
  - `ref/hr/run-payroll`, activity 16 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Record What the Run Taught**
  - `ref/hr/run-payroll`, activity 17 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)

## What to record

Each pay period leaves its dates, the cutoff and the payday, every
approved change gathered with its source, the time and variable pay with
the manager who approved each item and anything held for the next run
with its reason, the deductions applied in order, each employee's pay
from gross to net, and the register set beside the last period with
every movement past the threshold traced to its cause. Beside the
register sit the finance controller's check and the approver's approval,
and after them the payment file built from the approved register, the
payslips issued, the withholding paid and filed with its receipts, any
correction off cycle with the approval behind it, and the journal posted
with its totals agreed to the register. Each back pay, catch-up, refund,
leave pay and final pay leaves the working period by period with the tax
and deductions on it and the decision it carries out, and an overpayment
leaves the written notice the employee received before anything was
recovered. Each payroll year leaves the last adjustments with their
approvals, the new year's rates as the payroll manager confirmed them,
each person's totals, the reconciliation to the filings and to the
ledger with every difference named and corrected, the statements
produced and issued with their dates, and each question answered.
Nothing in the record shows this agent approving a register or releasing
money.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
