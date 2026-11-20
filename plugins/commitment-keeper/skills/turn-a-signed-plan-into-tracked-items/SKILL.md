---
name: turn-a-signed-plan-into-tracked-items
description: Takes the milestones a signed plan carries, or the fixes a failed control or an auditor's letter needs, and makes each one an item with one owner, one date and a state, traceable to the line of the plan or the finding it came from. Use it when running `ref/fin/run-the-external-audit` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Turn a signed plan into tracked items

## What it does

Takes the milestones a signed plan carries, or the fixes a failed
control or an auditor's letter needs, and makes each one an item with
one owner, one date and a state, traceable to the line of the plan or
the finding it came from.

## Where it happens

The agent does this in five activities across seven reference processes.
Each one names the activity as that process words it.

- **Load Each Fix Into the Tracker**
  - `ref/fin/run-the-external-audit`, activity 19 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
  - `ref/fin/test-a-financial-control`, activity 13 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Load the Actions into the Tracker**
  - `ref/hr/run-the-employee-survey`, activity 16 -
    [Run the Employee Survey](../../../../processes/human-resources/run-the-employee-survey.md)
- **Load the Plan into the Tracker**
  - `ref/hr/run-a-new-hires-first-months`, activity 4 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)
  - `ref/hr/run-a-performance-improvement-plan`, activity 10 -
    [Run a Performance Improvement Plan](../../../../processes/human-resources/run-a-performance-improvement-plan.md)
  - `ref/pc/write-the-value-creation-plan`, activity 13 -
    [Write the Value Creation Plan](../../../../processes/private-capital/write-the-value-creation-plan.md)
- **Record the Commitments**
  - `ref/prt/write-a-joint-plan`, activity 15 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)
- **Set the Milestones and the Dates**
  - `ref/prt/write-a-joint-plan`, activity 10 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)

## What to record

Each commitment as an item carrying one owner, one date and a state,
traceable to the line of the signed plan it came from. At every review,
the roll-call of all of them with the late ones counted. Each closed
commitment with the reason it was given up on and the date. The
decisions from the review with the new owners and the new dates, and
every move of a date with the review that moved it, so a commitment that
has slipped twice can be seen to have slipped twice. The review dates
set for the year, and whose calendars they landed on.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
