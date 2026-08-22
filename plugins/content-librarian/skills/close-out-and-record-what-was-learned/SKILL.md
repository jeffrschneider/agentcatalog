---
name: close-out-and-record-what-was-learned
description: The agent closes a change once the requester agrees it is done, and records what to repeat and what to avoid next time. Use it when running `ref/mkt/brand-refresh`, `ref/mkt/refresh-content` and `ref/mkt/website-content-update`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Close out and record what was learned

## What it does

The agent closes a change once the requester agrees it is done, and
records what to repeat and what to avoid next time.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Close out the Change**
  - `ref/mkt/website-content-update`, activity 12 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Record What Was Learned**
  - `ref/mkt/brand-refresh`, activity 26 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
  - `ref/mkt/refresh-content`, activity 22 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)

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
