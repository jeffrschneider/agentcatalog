---
name: read-every-commitment-out-loud
description: Reads every commitment at review with its owner, its date and its state, marked met, running, late or untouched, so nothing stays open by silence. Use it when running `ref/fin/test-a-financial-control` and 7 other reference processes.
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Read every commitment out loud

## What it does

Reads every commitment at review with its owner, its date and its state,
marked met, running, late or untouched, so nothing stays open by
silence.

## Where it happens

The agent does this in eleven activities across eight reference
processes. Each one names the activity as that process words it.

- **Chase Each Action to Its Date**
  - `ref/sup/coach-a-support-person`, activity 11 -
    [Coach a Support Person](../../../../processes/customer-support/coach-a-support-person.md)
- **Chase Each Fix to Its Date**
  - `ref/fin/test-a-financial-control`, activity 14 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Follow Up the Actions**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 18 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **Hold Each Check-In**
  - `ref/hr/run-a-performance-improvement-plan`, activity 12 -
    [Run a Performance Improvement Plan](../../../../processes/human-resources/run-a-performance-improvement-plan.md)
- **Read Out Last Time's Actions**
  - `ref/sup/coach-a-support-person`, activity 4 -
    [Coach a Support Person](../../../../processes/customer-support/coach-a-support-person.md)
- **Read Progress Against the Plan**
  - `ref/pc/write-the-value-creation-plan`, activity 15 -
    [Write the Value Creation Plan](../../../../processes/private-capital/write-the-value-creation-plan.md)
- **Read Progress on the Value Creation Plan**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 4 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **Read the Commitments**
  - `ref/prt/review-a-joint-plan`, activity 5 -
    [Review a Joint Plan](../../../../processes/partners/review-a-joint-plan.md)
- **Read the Open Actions**
  - `ref/pc/prepare-and-hold-a-board-meeting`, activity 5 -
    [Prepare and Hold a Board Meeting](../../../../processes/private-capital/prepare-and-hold-a-board-meeting.md)
- **Record the Check-In**
  - `ref/hr/run-a-new-hires-first-months`, activity 7 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)
- **Review the Actions**
  - `ref/hr/run-the-employee-survey`, activity 18 -
    [Run the Employee Survey](../../../../processes/human-resources/run-the-employee-survey.md)

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
