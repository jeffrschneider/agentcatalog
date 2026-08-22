---
name: test-decision
description: Reads a finished test and calls a winner, no difference, or more time, then puts the winner in place of what was running and takes the losing versions off. Use it when running `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Test decision

## What it does

Reads a finished test and calls a winner, no difference, or more time,
then puts the winner in place of what was running and takes the losing
versions off.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Call the Winner**
  - `ref/mkt/test-ad-creative`, activity 16 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Roll out the Winner**
  - `ref/mkt/test-ad-creative`, activity 17 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
