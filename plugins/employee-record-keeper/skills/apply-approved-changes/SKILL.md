---
name: apply-approved-changes
description: Checks each change for the asker's authority and its evidence, finds what else it touches, and applies it on its effective date with the old value kept, taking every decision about a person from the record of the named person who made it. Use it when running `ref/hr/change-an-employee-record`, `ref/hr/change-an-employees-pay` and `ref/hr/change-the-organization-structure`.
license: CC-BY-4.0
metadata:
  agent: employee-record-keeper
  agent-version: "1"
---

# Apply approved changes

## What it does

Checks each change for the asker's authority and its evidence, finds
what else it touches, and applies it on its effective date with the old
value kept, taking every decision about a person from the record of the
named person who made it. It tells the employee what changed and closes
the change on the record.

## Where it happens

The agent does this in nine activities across three reference processes.
Each one names the activity as that process words it.

- **Apply the Change on Its Date**
  - `ref/hr/change-an-employee-record`, activity 7 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Apply the Change to the Record**
  - `ref/hr/change-an-employees-pay`, activity 10 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)
- **Check the Authority to Ask**
  - `ref/hr/change-an-employee-record`, activity 2 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Check the Evidence**
  - `ref/hr/change-an-employee-record`, activity 3 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Close the Change on the Record**
  - `ref/hr/change-an-employee-record`, activity 13 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Find What Else the Change Touches**
  - `ref/hr/change-an-employee-record`, activity 6 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Record the Change on One Date**
  - `ref/hr/change-the-organization-structure`, activity 16 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **Take in the Change**
  - `ref/hr/change-an-employee-record`, activity 1 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Tell the Employee What Changed**
  - `ref/hr/change-an-employee-record`, activity 12 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)

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
