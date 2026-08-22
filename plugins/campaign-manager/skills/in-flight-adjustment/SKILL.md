---
name: in-flight-adjustment
description: Reads what is running against what it was meant to do, says which lines should give money up and which should take it, moves the money, and swaps out creative that has stopped working. Use it when running `ref/mkt/reallocate-media-spend` and `ref/mkt/social-campaign`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# In flight adjustment

## What it does

Reads what is running against what it was meant to do, says which lines
should give money up and which should take it, moves the money, and
swaps out creative that has stopped working.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Name the Candidate Moves**
  - `ref/mkt/reallocate-media-spend`, activity 4 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)
- **Optimize**
  - `ref/mkt/social-campaign`, activity 11 -
    [Run Social Media Campaign](../../../../processes/marketing/social-campaign.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
