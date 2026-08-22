---
name: take-in-a-signal-to-read
description: Takes in the signal that asks for a reading, with the account it is against and what raised it, so the reading answers a question somebody actually asked. Use it when running `ref/sls/spot-an-expansion`.
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Take in a signal to read

## What it does

Takes in the signal that asks for a reading, with the account it is
against and what raised it, so the reading answers a question somebody
actually asked.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Take in the Signal**
  - `ref/sls/spot-an-expansion`, activity 1 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)

## What to record

Per reading: the metered thing, the entitlement it is set against, the
periods compared, the system it was read from and the date it was read.
Per account: where use sits against each limit, which teams began using
what and when, which stopped and when, and the direction of travel on
each line. A reading is dated rather than reused, so a run that confirms
an opening or watches a risk turn records a fresh read at today's date
and keeps the earlier one beside it. Anyone auditing a decision can put
the reading next to the agreement and get the same answer.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
