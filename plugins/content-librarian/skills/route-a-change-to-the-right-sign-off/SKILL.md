---
name: route-a-change-to-the-right-sign-off
description: The agent works out whether a requested change is a small edit or needs a fuller process and who has to sign it, and puts every merge and retirement in front of a person before anything comes down. Use it when running `ref/mkt/refresh-content` and `ref/mkt/website-content-update`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Route a change to the right sign off

## What it does

The agent works out whether a requested change is a small edit or needs
a fuller process and who has to sign it, and puts every merge and
retirement in front of a person before anything comes down.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Approve the Merges and the Retirements**
  - `ref/mkt/refresh-content`, activity 8 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Route the Change**
  - `ref/mkt/website-content-update`, activity 3 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)

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
