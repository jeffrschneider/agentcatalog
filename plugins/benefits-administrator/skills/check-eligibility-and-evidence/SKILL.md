---
name: check-eligibility-and-evidence
description: Checks the employee and each dependent against the plan rules and asks only for the evidence the plan names, held where only the named benefits people may open it, with any evidence of good health sent from the employee to the carrier directly. Use it when running `ref/hr/enroll-an-employee-in-benefits` and `ref/hr/run-benefits-open-enrollment`.
license: CC-BY-4.0
metadata:
  agent: benefits-administrator
  agent-version: "1"
---

# Check eligibility and evidence

## What it does

Checks the employee and each dependent against the plan rules and asks
only for the evidence the plan names, held where only the named benefits
people may open it, with any evidence of good health sent from the
employee to the carrier directly.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Ask for the Evidence the Plan Requires**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 6 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
- **Check Eligibility**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 2 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
- **Check Eligibility and Evidence**
  - `ref/hr/run-benefits-open-enrollment`, activity 13 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)

## What to record

Each open enrollment leaves the timetable counted back from the first
day of the plan year, the figures sent to the broker with nothing that
identifies anyone's health, the plans, rates, employee costs and
eligibility rules set up and tested before the window opened, the notice
each employee received and its date, each election as the employee
confirmed it, each reminder sent, each dependent checked with the
evidence asked for, each default applied with the reminders that came
before it, each carrier file and its confirmation matched employee by
employee and dependent by dependent, each deduction sent to payroll with
its start date, and each first bill matched to the enrollments and the
deductions. Each enrollment for a new hire or a life event leaves the
event and its date, the eligibility check, the window and its dates, the
options the employee was told, the elections, the evidence kept and what
was deleted, the carriers' confirmations, the deductions sent and the
confirmation the employee received. Each leave leaves how each benefit
continued, paused or was paid for, and the date normal benefits
returned, with nothing about the reason for the leave. Each leaver
leaves each end date sent to its carrier and payroll and each
continuation notice with the date it was sent. Nothing in the record
shows this agent choosing a plan, deciding a disputed request or asking
about anyone's health.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
