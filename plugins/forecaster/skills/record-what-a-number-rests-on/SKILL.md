---
name: record-what-a-number-rests-on
description: Writes down what a number rests on, which means the assumptions, the boundary, the method, the window it covers, and what would reopen it. Use it when running `ref/mkt/annual-marketing-plan` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Record what a number rests on

## What it does

Writes down what a number rests on, which means the assumptions, the
boundary, the method, the window it covers, and what would reopen it.

## Where it happens

The agent does this in five activities across six reference processes.
Each one names the activity as that process words it.

- **Record What the Budget Rests On**
  - `ref/mkt/set-marketing-budget`, activity 15 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Record What the Plan Rests On**
  - `ref/mkt/annual-marketing-plan`, activity 16 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/media-plan`, activity 14 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Record What the Review Rests On**
  - `ref/mkt/quarterly-business-review`, activity 16 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Record What the Round Rests On**
  - `ref/mkt/prioritize-initiatives`, activity 16 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Write down the Sizing**
  - `ref/mkt/size-market-opportunity`, activity 13 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
