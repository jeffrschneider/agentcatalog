---
name: take-in-requests-and-score-them
description: The agent collects what every agent wants made and scores each candidate against the goals already set and the evidence behind it. Use it when running `ref/mkt/content-calendar`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Take in requests and score them

## What it does

The agent collects what every agent wants made and scores each candidate
against the goals already set and the evidence behind it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Collect the Topic Candidates**
  - `ref/mkt/content-calendar`, activity 4 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Score the Candidates**
  - `ref/mkt/content-calendar`, activity 8 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)

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
