---
name: read-what-is-committed-and-what-is-free
description: Reports what the period has already committed, what has been spent against it, and what is still free to place. Use it when running `ref/mkt/plan-marketing-capacity`, `ref/mkt/prioritize-initiatives` and `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Read what is committed and what is free

## What it does

Reports what the period has already committed, what has been spent
against it, and what is still free to place.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **List the Committed Work**
  - `ref/mkt/plan-marketing-capacity`, activity 2 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Read the Current Position**
  - `ref/mkt/reallocate-media-spend`, activity 3 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)
- **Work out What Is Free**
  - `ref/mkt/prioritize-initiatives`, activity 5 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
