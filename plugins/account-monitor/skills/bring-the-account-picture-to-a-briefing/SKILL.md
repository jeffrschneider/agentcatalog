---
name: bring-the-account-picture-to-a-briefing
description: The agent sits in the briefing that opens a run and gives every agent that will act the same picture of the account at the same time. Use it when running `ref/mkt/onboarding-email-program` and `ref/mkt/win-loss-analysis`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Bring the account picture to a briefing

## What it does

The agent sits in the briefing that opens a run and gives every agent
that will act the same picture of the account at the same time.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Brief the Agents that Act**
  - `ref/mkt/onboarding-email-program`, activity 5 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Brief the Study**
  - `ref/mkt/win-loss-analysis`, activity 3 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)

## What to record

For each question it answers, it records the account, what was asked,
the answer, the date, and every system it read with the value it found
and when that value was current. A milestone answer names the milestone
list at its version and says which of those milestones the account has
met. A risk signal is recorded whichever way it was judged, with the
reading that settled it. Anything it could not read is recorded as
unread instead of being left out of the answer.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
