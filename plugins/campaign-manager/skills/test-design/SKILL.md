---
name: test-design
description: Names the one element a test changes and what it should improve, sets how much exposure it needs and how big a difference has to be before it counts, and says what that exposure will cost and whether to pay it. Use it when running `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Test design

## What it does

Names the one element a test changes and what it should improve, sets
how much exposure it needs and how big a difference has to be before it
counts, and says what that exposure will cost and whether to pay it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Commit the Test Budget**
  - `ref/mkt/test-ad-creative`, activity 6 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Name the Change to Test**
  - `ref/mkt/test-ad-creative`, activity 3 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Set the Evidence Bar**
  - `ref/mkt/test-ad-creative`, activity 5 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
