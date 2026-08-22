---
name: decide-what-happens-to-each-page
description: The agent decides for each page or surface whether it is updated, merged into another, retired, replaced or left alone, and records the reason behind every decision. Use it when running `ref/mkt/brand-refresh` and `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Decide what happens to each page

## What it does

The agent decides for each page or surface whether it is updated, merged
into another, retired, replaced or left alone, and records the reason
behind every decision.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Decide What Happens to Each Page**
  - `ref/mkt/refresh-content`, activity 7 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Decide What Happens to Each Surface**
  - `ref/mkt/brand-refresh`, activity 8 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)

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
