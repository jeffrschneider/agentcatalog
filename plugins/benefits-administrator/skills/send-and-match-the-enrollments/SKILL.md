---
name: send-and-match-the-enrollments
description: Sends each enrollment to its carrier and each deduction to payroll before the cutoff, matches each carrier's confirmation and first bill to the elections and the deductions, sends the employee a confirmation of the cover and its cost, and closes the enrollment on the record. Use it when running `ref/hr/enroll-an-employee-in-benefits` and `ref/hr/run-benefits-open-enrollment`.
license: CC-BY-4.0
metadata:
  agent: benefits-administrator
  agent-version: "1"
---

# Send and match the enrollments

## What it does

Sends each enrollment to its carrier and each deduction to payroll
before the cutoff, matches each carrier's confirmation and first bill to
the elections and the deductions, sends the employee a confirmation of
the cover and its cost, and closes the enrollment on the record.

## Where it happens

The agent does this in eight activities across two reference processes.
Each one names the activity as that process words it.

- **Close the Enrollment on the Record**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 16 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
- **Confirm the Carriers Hold the Coverage**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 14 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
- **Confirm the Carriers Hold the Elections**
  - `ref/hr/run-benefits-open-enrollment`, activity 17 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Match the First Bills**
  - `ref/hr/run-benefits-open-enrollment`, activity 18 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Record What the Enrollment Taught**
  - `ref/hr/run-benefits-open-enrollment`, activity 19 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Send the Deductions to Payroll**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 11 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
  - `ref/hr/run-benefits-open-enrollment`, activity 16 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Send the Elections to the Carriers**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 10 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)
  - `ref/hr/run-benefits-open-enrollment`, activity 15 -
    [Run Benefits Open Enrollment](../../../../processes/human-resources/run-benefits-open-enrollment.md)
- **Send the Employee a Confirmation**
  - `ref/hr/enroll-an-employee-in-benefits`, activity 15 -
    [Enroll an Employee in Benefits](../../../../processes/human-resources/enroll-an-employee-in-benefits.md)

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
