---
name: track-probation
description: Confirms the date a probation closes and the steps the contract sets, records the outcome the manager decided with who decided it and when, and hands an ended employment to the offboarding. Use it when running `ref/hr/run-a-new-hires-first-months`.
license: CC-BY-4.0
metadata:
  agent: employee-record-keeper
  agent-version: "1"
---

# Track probation

## What it does

Confirms the date a probation closes and the steps the contract sets,
records the outcome the manager decided with who decided it and when,
and hands an ended employment to the offboarding.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Confirm the Probation Terms**
  - `ref/hr/run-a-new-hires-first-months`, activity 10 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)
- **Hand an Ended Employment to Offboarding**
  - `ref/hr/run-a-new-hires-first-months`, activity 15 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)
- **Record the Outcome**
  - `ref/hr/run-a-new-hires-first-months`, activity 14 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)

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
