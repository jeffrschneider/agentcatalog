---
name: hand-the-decision-to-whoever-acts-on-it
description: Passes a settled decision to the agents that have to act on it, and hands an owned item to its named owner with a date to review it. Use it when running `ref/mkt/brief-executive-leadership` and `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: capacity-manager
  agent-version: "1"
---

# Hand the decision to whoever acts on it

## What it does

Passes a settled decision to the agents that have to act on it, and
hands an owned item to its named owner with a date to review it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand It to the Owner**
  - `ref/mkt/select-marketing-technology`, activity 20 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Hand the Decisions On**
  - `ref/mkt/brief-executive-leadership`, activity 19 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)

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
