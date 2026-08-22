---
name: match-published-work-to-the-questions-it-answers
description: The agent sets what has been published against the questions buyers ask, says which piece answers which question, names the questions with nothing behind them, and sends each gap to the agent that can close it. Use it when running `ref/mkt/brand-audit` and `ref/mkt/map-buyer-journey`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Match published work to the questions it answers

## What it does

The agent sets what has been published against the questions buyers ask,
says which piece answers which question, names the questions with
nothing behind them, and sends each gap to the agent that can close it.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Find the Gaps**
  - `ref/mkt/map-buyer-journey`, activity 13 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Hand the Gaps to the Owners**
  - `ref/mkt/brand-audit`, activity 16 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)
- **Inventory the Content against the Map**
  - `ref/mkt/map-buyer-journey`, activity 12 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)

## What to record

The inventory at a version every time it is rebuilt, with each live page
carrying what it was made to do, the date it last changed, what it is
doing now, and where every figure came from. The refresh cycle's list,
giving the reason each page is on it, and a line for the pages that were
looked at and left for a later cycle. A decision record for every merge,
retirement and redirect, naming the version that came down, what now
stands at its address, and the person who said so. A page it could not
measure is recorded as unmeasured, with the reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
