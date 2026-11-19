---
name: check-the-pay
description: Compares the register with the last period and traces every movement to an approved change, confirms the first pay at a new rate and a leaver's final pay against the record with the finance controller, and corrects an error off cycle once a person releases or approves it. Use it when running `ref/hr/change-an-employees-pay`, `ref/hr/offboard-a-leaver` and `ref/hr/run-payroll`.
license: CC-BY-4.0
metadata:
  agent: payroll-administrator
  agent-version: "1"
---

# Check the pay

## What it does

Compares the register with the last period and traces every movement to
an approved change, confirms the first pay at a new rate and a leaver's
final pay against the record with the finance controller, and corrects
an error off cycle once a person releases or approves it.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Final Pay**
  - `ref/hr/offboard-a-leaver`, activity 9 -
    [Offboard a Leaver](../../../../processes/human-resources/offboard-a-leaver.md)
- **Compare the Register with the Last Period**
  - `ref/hr/run-payroll`, activity 6 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Confirm the First Pay at the New Rate**
  - `ref/hr/change-an-employees-pay`, activity 13 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)
- **Correct an Error Off Cycle**
  - `ref/hr/run-payroll`, activity 15 -
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
