---
name: check-the-accounts-a-plan-names
description: Picks the named accounts and segments two sides will work together, and reads them against coverage for overlap, for conflicts and for accounts already spoken for. Use it when running `ref/prt/write-a-joint-plan`.
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Check the accounts a plan names

## What it does

Picks the named accounts and segments two sides will work together, and
reads them against coverage for overlap, for conflicts and for accounts
already spoken for.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Accounts Against Coverage**
  - `ref/prt/write-a-joint-plan`, activity 6 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)
- **Pick the Accounts and Segments**
  - `ref/prt/write-a-joint-plan`, activity 5 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)

## What to record

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
