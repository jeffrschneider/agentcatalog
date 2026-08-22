---
name: write-a-message-sequence
description: The agent writes the messages a program sends and the order they go in, and rewrites the ones the numbers argue against once it is running. Use it when running `ref/mkt/nurture-sequence` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: copywriter
  agent-version: "1"
---

# Write a message sequence

## What it does

The agent writes the messages a program sends and the order they go in,
and rewrites the ones the numbers argue against once it is running.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Produce the Messages**
  - `ref/mkt/nurture-sequence`, activity 7 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Tune the Branches**
  - `ref/mkt/nurture-sequence`, activity 16 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Write the Sequence**
  - `ref/mkt/win-back-campaign`, activity 8 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

Every draft at a version, and the DONE records of the patterns it works
inside. A claim it uses cites the register entry it came from.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
