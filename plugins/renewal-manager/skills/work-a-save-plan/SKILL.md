---
name: work-a-save-plan
description: Agrees the plan that answers a named risk, then closes the risk out when the plan turns it or puts it up for a decision when it does not. Use it when running `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: renewal-manager
  agent-version: "1"
---

# Work a save plan

## What it does

Agrees the plan that answers a named risk, then closes the risk out when
the plan turns it or puts it up for a decision when it does not.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Agree the Save Plan**
  - `ref/sls/work-a-churn-risk`, activity 8 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Close or Escalate the Risk**
  - `ref/sls/work-a-churn-risk`, activity 14 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)

## What to record

Per renewal: the clock, opened from the agreement's own dates, with the
date the position is due. The agreement as read, with a settled reading
attached to any clause that could be read two ways. The entitlements at
their signed level with the amendments. The commitments made at
signature and still open, each with who owes it and since when. The
shape of the next term and the reason for it. The ask and the floor at
the version a person approved, with that person named. The brief at a
version, with the usage and the standing attached rather than
summarized. The customer's own words, kept rather than replaced by a
summary. What carries over, what is dropped, what is added. A smaller
term recorded beside the old price with its distance from the floor
stated. The signed agreement, and the booked term set against it line
for line. Why the term grew, held or shrank, in a form the next renewal
can read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
