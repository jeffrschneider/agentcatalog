---
name: check-each-accounts-standing
description: Support history, renewal position, contract terms. Use it when running `ref/mkt/customer-reference`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Check Each Account's Standing

## What happens

Support history, renewal position, contract terms.

## Where it happens

- `ref/mkt/customer-reference`, activity 4 -
  [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)

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
