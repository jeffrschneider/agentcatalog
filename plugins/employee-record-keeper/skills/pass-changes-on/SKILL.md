---
name: pass-changes-on
description: Passes every approved change to payroll before its cut-off, to benefits and to access, gathers the changes each pay run needs, and reads each system back field by field against the record. Use it when running `ref/hr/change-an-employee-record`, `ref/hr/change-an-employees-pay` and `ref/hr/run-payroll`.
license: CC-BY-4.0
metadata:
  agent: employee-record-keeper
  agent-version: "1"
---

# Pass changes on

## What it does

Passes every approved change to payroll before its cut-off, to benefits
and to access, gathers the changes each pay run needs, and reads each
system back field by field against the record.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Confirm Each System Shows the Change**
  - `ref/hr/change-an-employee-record`, activity 11 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Gather the Approved Changes**
  - `ref/hr/run-payroll`, activity 2 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Pass the Change to Access**
  - `ref/hr/change-an-employee-record`, activity 10 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Pass the Change to Benefits**
  - `ref/hr/change-an-employee-record`, activity 9 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Pass the Change to Payroll**
  - `ref/hr/change-an-employee-record`, activity 8 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
  - `ref/hr/change-an-employees-pay`, activity 11 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)

## What to record

Each new hire leaves one record created from the signed offer after a
check for an old record of the same person, each form filed, the outcome
of the right to work check with the person who examined the documents
and the end date of any permission that expires, the documents kept in
the restricted store, and the pay, the tax details, the bank account and
the benefits eligibility passed on. Each change leaves who asked, the
authority they had, the evidence and the decision record it rests on,
the approval, what else it touched, the new value with its effective
date and the old one kept with its dates, each system it reached and
read back, and the notice the employee received. A refused change leaves
the rule that refused it and who may ask. A probation leaves its closing
date and terms, the outcome, who decided it and the date, and for an
ended employment the hand-off to the leaving. A reorganization leaves
every role, manager and team changed on its effective date, with each
difference from the recorded decisions listed and corrected. A records
request leaves the request, the identity check, every record found, each
holder of a restricted record asked, other people's details set aside,
each correction or deletion made, what was released and the reason for
anything withheld, with the privacy lead's decision and approval beside
it, and when it was sent. An audit leaves the hold in place on every
record in scope, and only the records and fields each request covered.
An access review leaves everyone who can open each restricted record
checked against the named people, each person marked to go, and the
period's openings read against the named people. Nothing in the record
shows this agent reading what a restricted record says or making a
decision about a person.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
