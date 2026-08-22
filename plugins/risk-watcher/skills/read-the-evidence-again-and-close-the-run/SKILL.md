---
name: read-the-evidence-again-and-close-the-run
description: Reads the same evidence again after the plan was delivered to see whether the signal turned, then closes the risk or puts it up, and records the save or the departure with what was tried, what it cost and what the customer said. Use it when running `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: risk-watcher
  agent-version: "1"
---

# Read the evidence again and close the run

## What it does

Reads the same evidence again after the plan was delivered to see
whether the signal turned, then closes the risk or puts it up, and
records the save or the departure with what was tried, what it cost and
what the customer said.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Close or Escalate the Risk**
  - `ref/sls/work-a-churn-risk`, activity 14 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Record the Save or the Departure**
  - `ref/sls/work-a-churn-risk`, activity 15 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Watch for the Signal to Turn**
  - `ref/sls/work-a-churn-risk`, activity 13 -
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
