---
name: match-a-request-to-its-account
description: The agent matches the sender of a support request to one customer and one account from the details already on file, and records the match as saying which account the request is about and proving nothing about who sent it. Use it when running `ref/sup/take-in-a-request`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Match a request to its account

## What it does

The agent matches the sender of a support request to one customer and
one account from the details already on file, and records the match as
saying which account the request is about and proving nothing about who
sent it. A sender who matches no account or more than one is reported as
unmatched.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Match the Sender to an Account**
  - `ref/sup/take-in-a-request`, activity 2 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)

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
