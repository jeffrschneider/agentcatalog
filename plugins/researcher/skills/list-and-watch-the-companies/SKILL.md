---
name: list-and-watch-the-companies
description: Finds every company that fits a written profile, whether it fits a sector thesis or is a buyer that would pay for a holding, and records the source each one was found in and the date that source was read. Use it when running `ref/pc/map-a-sector` and `ref/pc/plan-the-exit`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# List and watch the companies

## What it does

Finds every company that fits a written profile, whether it fits a
sector thesis or is a buyer that would pay for a holding, and records
the source each one was found in and the date that source was read. For
a buyer it says why the buyer would pay and what it has bought before.
It then watches the listed companies and records each sign that one may
be ready to talk, with its source and its date.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **List the Companies That Fit**
  - `ref/pc/map-a-sector`, activity 7 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **List the Likely Buyers**
  - `ref/pc/plan-the-exit`, activity 5 -
    [Plan the Exit](../../../../processes/private-capital/plan-the-exit.md)
- **Watch the Companies**
  - `ref/pc/map-a-sector`, activity 13 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
