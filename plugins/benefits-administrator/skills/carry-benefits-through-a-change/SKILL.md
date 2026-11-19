---
name: carry-benefits-through-a-change
description: Works out how each benefit continues while an employee is on leave and puts that arrangement in place, restores normal benefits and deductions on the return, and when someone leaves sends each end date to its carrier and payroll with the continuation notices by their deadline. Use it when running `ref/hr/manage-a-leave-of-absence` and `ref/hr/offboard-a-leaver`.
license: CC-BY-4.0
metadata:
  agent: benefits-administrator
  agent-version: "1"
---

# Carry benefits through a change

## What it does

Works out how each benefit continues while an employee is on leave and
puts that arrangement in place, restores normal benefits and deductions
on the return, and when someone leaves sends each end date to its
carrier and payroll with the continuation notices by their deadline.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **End or Continue the Benefits**
  - `ref/hr/offboard-a-leaver`, activity 11 -
    [Offboard a Leaver](../../../../processes/human-resources/offboard-a-leaver.md)
- **Put the Benefits Arrangement in Place**
  - `ref/hr/manage-a-leave-of-absence`, activity 12 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Restore Normal Benefits**
  - `ref/hr/manage-a-leave-of-absence`, activity 17 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Work Out Benefits During the Leave**
  - `ref/hr/manage-a-leave-of-absence`, activity 7 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)

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
