---
name: open-an-expansion-deal
description: Reads the account again before an opening is put to the customer, sets the timing against the contract they already hold, gets the go-ahead from inside, and opens the deal with its evidence on it. Use it when running `ref/sls/open-an-expansion-deal`.
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Open an expansion deal

## What it does

Reads the account again before an opening is put to the customer, sets
the timing against the contract they already hold, gets the go-ahead
from inside, and opens the deal with its evidence on it.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Get the Internal Go-Ahead**
  - `ref/sls/open-an-expansion-deal`, activity 11 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Open the Deal**
  - `ref/sls/open-an-expansion-deal`, activity 14 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Re-Read the Account**
  - `ref/sls/open-an-expansion-deal`, activity 2 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Set the Timing Against the Contract**
  - `ref/sls/open-an-expansion-deal`, activity 6 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)

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
