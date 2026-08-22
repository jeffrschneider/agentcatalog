---
name: put-cost-and-return-on-an-option
description: Works out what an option would cost and what it would return at each level of spend, with every assumption written down beside the number it produced. Use it when running `ref/mkt/annual-marketing-plan` and 11 other reference processes.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Put cost and return on an option

## What it does

Works out what an option would cost and what it would return at each
level of spend, with every assumption written down beside the number it
produced. A rate the agent cannot source is reported as unsourced rather
than filled in with a figure that looks reasonable.

## Where it happens

The agent does this in twelve activities across twelve reference
processes. Each one names the activity as that process words it.

- **Choose the Route**
  - `ref/mkt/engage-marketing-agency`, activity 2 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Cost Each Way of Closing the Gap**
  - `ref/mkt/plan-marketing-capacity`, activity 9 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Model Each Mix**
  - `ref/mkt/media-plan`, activity 7 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Price the Incentives**
  - `ref/mkt/channel-program`, activity 3 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
- **Price the Requests**
  - `ref/mkt/set-marketing-budget`, activity 5 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Put Numbers on Each Initiative**
  - `ref/mkt/annual-marketing-plan`, activity 7 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
- **Put Numbers on Each Option**
  - `ref/mkt/develop-marketing-strategy`, activity 7 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Put Numbers on Each Request**
  - `ref/mkt/prioritize-initiatives`, activity 7 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Put Numbers on the Choices**
  - `ref/mkt/brief-executive-leadership`, activity 9 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Put Numbers on the Proposed Changes**
  - `ref/mkt/quarterly-business-review`, activity 9 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Size What Each Move Returns**
  - `ref/mkt/reallocate-media-spend`, activity 6 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)
- **Work out the Whole Cost**
  - `ref/mkt/select-marketing-technology`, activity 15 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

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
