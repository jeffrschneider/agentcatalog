---
name: prepare-the-pay-period
description: Opens the pay period with its cutoff and payday, gathers every change approved since the last run, collects the time and variable pay each manager approved, and applies the benefit and other deductions in the order the rules set, starting each new deduction in the first period the plan allows. Use it when running `ref/hr/enroll-an-employee-in-benefits` and `ref/hr/run-payroll`.
license: CC-BY-4.0
metadata:
  agent: payroll-administrator
  agent-version: "1"
---

# Prepare the pay period

## What it does

Opens the pay period with its cutoff and payday, gathers every change
approved since the last run, collects the time and variable pay each
manager approved, and applies the benefit and other deductions in the
order the rules set, starting each new deduction in the first period the
plan allows.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Apply the Deductions**
  - `ref/hr/run-payroll`, activity 4 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Collect Time and Variable Pay**
  - `ref/hr/run-payroll`, activity 3 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Gather the Approved Changes**
  - `ref/hr/run-payroll`, activity 2 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Open the Pay Period**
  - `ref/hr/run-payroll`, activity 1 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Start the Deductions**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 12 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)

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
