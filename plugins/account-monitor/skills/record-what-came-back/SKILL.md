---
name: record-what-came-back
description: The agent takes the questions, objections and cancellation requests that arrive, reads the account behind each one, and records what was offered, what the account did, and the date. Use it when running `ref/mkt/churn-risk-play` and `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Record what came back

## What it does

The agent takes the questions, objections and cancellation requests that
arrive, reads the account behind each one, and records what was offered,
what the account did, and the date.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Answer What Comes Back**
  - `ref/mkt/pricing-change`, activity 11 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Record the Outcome**
  - `ref/mkt/churn-risk-play`, activity 11 -
    [Run Churn-Risk Play](../../../../processes/marketing/churn-risk-play.md)

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
