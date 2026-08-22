---
name: check-a-claim-against-the-systems
description: The agent takes a figure or a milestone somebody has stated and reads it back out of the systems that hold the record, saying whether it holds and naming anything it could not check. Use it when running `ref/mkt/customer-case-study` and `ref/mkt/onboarding-email-program`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Check a claim against the systems

## What it does

The agent takes a figure or a milestone somebody has stated and reads it
back out of the systems that hold the record, saying whether it holds
and naming anything it could not check.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Customer Is Active**
  - `ref/mkt/onboarding-email-program`, activity 13 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Verify the Customer's Results**
  - `ref/mkt/customer-case-study`, activity 7 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)

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
