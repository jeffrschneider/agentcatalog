---
name: work-out-pay
description: "Works out each employee's pay from gross to net under the tax and deduction rules for the place they work, and the amounts that run across periods: back pay from a past effective date, a catch-up or refund, pay during a leave and its return to normal, and a leaver's final pay. Use it when running `ref/hr/change-an-employees-pay` and 4 other reference processes."
license: CC-BY-4.0
metadata:
  agent: payroll-administrator
  agent-version: "1"
---

# Work out pay

## What it does

Works out each employee's pay from gross to net under the tax and
deduction rules for the place they work, and the amounts that run across
periods: back pay from a past effective date, a catch-up or refund, pay
during a leave and its return to normal, and a leaver's final pay.

## Where it happens

The agent does this in seven activities across five reference processes.
Each one names the activity as that process words it.

- **Restore Normal Pay**
  - `ref/hr/manage-a-leave-of-absence`, activity 16 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Set the Leave Pay in Payroll**
  - `ref/hr/manage-a-leave-of-absence`, activity 11 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Work Out Any Back Pay**
  - `ref/hr/change-an-employees-pay`, activity 12 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)
- **Work Out Any Catch-Up or Refund**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 13 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
- **Work Out Gross to Net**
  - `ref/hr/run-payroll`, activity 5 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Work Out Pay During the Leave**
  - `ref/hr/manage-a-leave-of-absence`, activity 6 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Work Out the Final Pay**
  - `ref/hr/offboard-a-leaver`, activity 8 -
    [Offboard a Leaver](../../../../processes/human-resources/offboard-a-leaver.md)

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
