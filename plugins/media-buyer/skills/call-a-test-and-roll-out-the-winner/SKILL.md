---
name: call-a-test-and-roll-out-the-winner
description: Reads a finished test against the bar that was set and says whether there is a winner, no difference, or more time needed, then puts the winning version in place of what was running and turns the rest off. Use it when running `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Call a test and roll out the winner

## What it does

Reads a finished test against the bar that was set and says whether
there is a winner, no difference, or more time needed, then puts the
winning version in place of what was running and turns the rest off.

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

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
