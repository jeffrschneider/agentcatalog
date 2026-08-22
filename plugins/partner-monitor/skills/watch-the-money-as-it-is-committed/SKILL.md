---
name: watch-the-money-as-it-is-committed
description: Watches a fund while the period runs and says what is approved, what is claimed and what is still free. Use it when running `ref/prt/allocate-the-fund`.
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Watch the money as it is committed

## What it does

Watches a fund while the period runs and says what is approved, what is
claimed and what is still free.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Watch the Fund as It Is Committed**
  - `ref/prt/allocate-the-fund`, activity 14 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)

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
