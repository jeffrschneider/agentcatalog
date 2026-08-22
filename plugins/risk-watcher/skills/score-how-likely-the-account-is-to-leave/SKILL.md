---
name: score-how-likely-the-account-is-to-leave
description: Scores the account against the risk model at a version, and keeps scoring it on a cadence while a renewal conversation is open, so what the customer says back to an offer is read against the same evidence. Use it when running `ref/sls/close-a-renewal` and `ref/sls/open-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: risk-watcher
  agent-version: "1"
---

# Score how likely the account is to leave

## What it does

Scores the account against the risk model at a version, and keeps
scoring it on a cadence while a renewal conversation is open, so what
the customer says back to an offer is read against the same evidence.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Score the Risk of Leaving**
  - `ref/sls/open-a-renewal`, activity 7 -
    [Open a Renewal](../../../../processes/sales/open-a-renewal.md)
- **Work the Response**
  - `ref/sls/close-a-renewal`, activity 9 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)

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
