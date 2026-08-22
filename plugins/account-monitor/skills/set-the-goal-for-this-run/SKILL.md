---
name: set-the-goal-for-this-run
description: The milestones this customer has to reach. Use it when running `ref/mkt/onboarding-email-program`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Set the Goal for This Run

## What happens

The milestones this customer has to reach.

## Where it happens

- `ref/mkt/onboarding-email-program`, activity 3 -
  [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)

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
