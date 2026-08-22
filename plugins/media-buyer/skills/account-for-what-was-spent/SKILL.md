---
name: account-for-what-was-spent
description: Reports what the paid buy spent by campaign and channel and what came back from it, and confirms the figures that name the buy in another agent's report before that report goes out. Use it when running `ref/mkt/marketing-performance-report`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Account for what was spent

## What it does

Reports what the paid buy spent by campaign and channel and what came
back from it, and confirms the figures that name the buy in another
agent's report before that report goes out.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Account for the Paid Spend**
  - `ref/mkt/marketing-performance-report`, activity 4 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Check the Account**
  - `ref/mkt/marketing-performance-report`, activity 12 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
