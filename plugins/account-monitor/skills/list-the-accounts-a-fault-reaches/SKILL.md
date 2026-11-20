---
name: list-the-accounts-a-fault-reaches
description: The agent lists every account a confirmed bug or an incident affects, from the cases on it and what engineering confirmed, each with its plan, its entitlement and its owner, and reads each affected account's agreement for any notice it promises on an outage. Use it when running `ref/sup/report-a-confirmed-bug` and `ref/sup/tell-affected-customers`.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# List the accounts a fault reaches

## What it does

The agent lists every account a confirmed bug or an incident affects,
from the cases on it and what engineering confirmed, each with its plan,
its entitlement and its owner, and reads each affected account's
agreement for any notice it promises on an outage.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **List the Accounts Affected**
  - `ref/sup/report-a-confirmed-bug`, activity 5 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **List the Affected Accounts**
  - `ref/sup/tell-affected-customers`, activity 2 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Read What Each Agreement Promises**
  - `ref/sup/tell-affected-customers`, activity 4 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)

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
