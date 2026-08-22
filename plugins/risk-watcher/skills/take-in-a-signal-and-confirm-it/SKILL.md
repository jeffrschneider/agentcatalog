---
name: take-in-a-signal-and-confirm-it
description: Takes in a signal that a customer may be leaving and tests it against the account record before anybody is told. Use it when running `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: risk-watcher
  agent-version: "1"
---

# Take in a signal and confirm it

## What it does

Takes in a signal that a customer may be leaving and tests it against
the account record before anybody is told. A signal the record
contradicts closes the run there, with the contradiction written down.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Confirm the Signal**
  - `ref/sls/work-a-churn-risk`, activity 2 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Take in the Risk Signal**
  - `ref/sls/work-a-churn-risk`, activity 1 -
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
