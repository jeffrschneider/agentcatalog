---
name: prepare-the-plan-year
description: Opens the renewal with its timetable counted back from the first day of the plan year, sends the broker the enrollment figures the carriers need with no one's health identified, and sets up and tests the plans, rates and eligibility rules the named people chose before the window opens. Use it when running `ref/hr/run-benefits-open-enrollment`.
license: CC-BY-4.0
metadata:
  agent: benefits-administrator
  agent-version: "1"
---

# Prepare the plan year

## What it does

Opens the renewal with its timetable counted back from the first day of
the plan year, sends the broker the enrollment figures the carriers need
with no one's health identified, and sets up and tests the plans, rates
and eligibility rules the named people chose before the window opens.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Open the Renewal**
  - `ref/hr/run-benefits-open-enrollment`, activity 1 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Send the Enrollment Figures**
  - `ref/hr/run-benefits-open-enrollment`, activity 3 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Set Up the Plans for the New Year**
  - `ref/hr/run-benefits-open-enrollment`, activity 9 -
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
