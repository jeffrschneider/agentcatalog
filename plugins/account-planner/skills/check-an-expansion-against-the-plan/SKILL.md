---
name: check-an-expansion-against-the-plan
description: "Reads an opening somebody else spotted against the open deals and against the plan: whether anybody is already on the same ground, roughly what it could be worth, and whether the plan already says to sell it. Use it when running `ref/sls/spot-an-expansion`."
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Check an expansion against the plan

## What it does

Reads an opening somebody else spotted against the open deals and
against the plan: whether anybody is already on the same ground, roughly
what it could be worth, and whether the plan already says to sell it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check It Against the Account Plan**
  - `ref/sls/spot-an-expansion`, activity 13 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)
- **Check Nobody Is Already On It**
  - `ref/sls/spot-an-expansion`, activity 8 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)
- **Size What It Could Be Worth**
  - `ref/sls/spot-an-expansion`, activity 9 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)

## What to record

The account read at a version, every line naming the system or document
it came from and the date that value was current, with the questions
nothing answered left standing as unknown. The plan at a version: each
opportunity with the evidence for it and against it, its buyer or the
note that it has none, its size in a confidence band, the order and what
each step depends on the one before it delivering, the assumptions
written as testable statements, the risks and what the plan does about
each, the moves with their owners and dates, and the asks naming who had
to agree. The signed version names both signers and the date. At review,
each plan is scored against what it said when it was signed, and every
decision records who made it, on what evidence, and anyone who
disagreed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
