---
name: give-finance-the-payroll-figures
description: "Gives finance the figures that fund the payroll account and reconcile it: each approved register's total, payday and pay group with the approval behind it, the net pay and withholding the account pays, the payments returned or not yet presented after payday, and each period's approved registers and payments for the monthly reconciliation. Use it when running `ref/fin/fund-the-payroll` and `ref/fin/reconcile-a-balance-sheet-account`."
license: CC-BY-4.0
metadata:
  agent: payroll-administrator
  agent-version: "1"
---

# Give finance the payroll figures

## What it does

Gives finance the figures that fund the payroll account and reconcile
it: each approved register's total, payday and pay group with the
approval behind it, the net pay and withholding the account pays, the
payments returned or not yet presented after payday, and each period's
approved registers and payments for the monthly reconciliation. It
changes nothing in finance's records and moves no money.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Total and the Payday**
  - `ref/fin/fund-the-payroll`, activity 2 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Explain What Is Left in the Account**
  - `ref/fin/fund-the-payroll`, activity 13 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Supply the Payroll Records**
  - `ref/fin/reconcile-a-balance-sheet-account`, activity 4 -
    [Reconcile a Balance Sheet Account](../../../../processes/finance/reconcile-a-balance-sheet-account.md)
- **Take In the Approved Register**
  - `ref/fin/fund-the-payroll`, activity 1 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)

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
