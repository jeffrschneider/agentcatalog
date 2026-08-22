---
name: give-every-piece-of-work-a-holder
description: Sorts the work by whether it needs a person or could be held by an agent, gives every piece in the period a holder, and names what is left with no holder and what happens to it. Use it when running `ref/mkt/plan-marketing-capacity`.
license: CC-BY-4.0
metadata:
  agent: capacity-manager
  agent-version: "1"
---

# Give every piece of work a holder

## What it does

Sorts the work by whether it needs a person or could be held by an
agent, gives every piece in the period a holder, and names what is left
with no holder and what happens to it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Match the Work to Holders**
  - `ref/mkt/plan-marketing-capacity`, activity 12 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Name the Gaps that Remain**
  - `ref/mkt/plan-marketing-capacity`, activity 13 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Sort the Activities by Who Can Hold Them**
  - `ref/mkt/plan-marketing-capacity`, activity 7 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)

## What to record

It leaves the book of work at a version for each period, with every
request carrying the date it arrived and its current state, and every
committed run carrying the agents it needs and the dates it holds. Every
commitment it makes is recorded with the date it was made and what it
displaced, and every commitment that changes is recorded the same way.
It records what each activity actually took against the run it came
from, so the department's estimates come from its own history. The room
left in the period is restated whenever a commitment lands or moves. A
request the department could not take is recorded with the reason and
the date, and it stays in the book.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
