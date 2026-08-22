---
name: set-the-severity-and-tell-the-owner
description: Sets how bad it is against the severity scale at a version, with the date somebody must act by, and tells the account owner inside the time the policy sets. Use it when running `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: risk-watcher
  agent-version: "1"
---

# Set the severity and tell the owner

## What it does

Sets how bad it is against the severity scale at a version, with the
date somebody must act by, and tells the account owner inside the time
the policy sets. The owner gets the reason and the evidence, not a
score.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Set the Severity and the Clock**
  - `ref/sls/work-a-churn-risk`, activity 6 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Tell the Account Owner**
  - `ref/sls/work-a-churn-risk`, activity 7 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)

## What to record

Per risk: the signal, what raised it, the date, and the account it is
against. The confirmation against the account record, or the
contradiction that closed the run without anybody being told. One
reason, in words, with the evidence lines that support it, each naming
the system it was read from and the date. The severity, the scale
version it was set against, and the date somebody must act by. What the
account owner was told and when they were told it. The readings taken
again against the reason after the plan was delivered, set beside what
the customer was promised. Whether the risk cleared, stayed open or went
up, and a departure written with its reason, what was tried, what it
cost and what the customer said, readable by everyone who works
renewals.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
