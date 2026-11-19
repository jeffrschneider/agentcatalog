---
name: guard-the-restricted-records
description: Lists everyone who can open the health, investigation and background check records, checks each one against the named people allowed, and reads the log of who opened them without reading what the records say. Use it when running `ref/hr/review-access-to-employee-data`.
license: CC-BY-4.0
metadata:
  agent: employee-record-keeper
  agent-version: "1"
---

# Guard the restricted records

## What it does

Lists everyone who can open the health, investigation and background
check records, checks each one against the named people allowed, and
reads the log of who opened them without reading what the records say.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check Each Against the Named People**
  - `ref/hr/review-access-to-employee-data`, activity 6 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **List Who Can Open Restricted Records**
  - `ref/hr/review-access-to-employee-data`, activity 5 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)
- **Read Who Opened Restricted Records**
  - `ref/hr/review-access-to-employee-data`, activity 7 -
    [Review Access to Employee Data](../../../../processes/human-resources/review-access-to-employee-data.md)

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
