---
name: verify-the-customers-results
description: The numbers read from the systems that hold them. Use it when running `ref/mkt/customer-case-study`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Verify the Customer's Results

## What happens

The numbers read from the systems that hold them.

## Where it happens

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
