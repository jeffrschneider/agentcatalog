---
name: record-the-declines
description: Every request not committed, with its reason. Use it when running `ref/mkt/prioritize-initiatives`.
license: CC-BY-4.0
metadata:
  agent: capacity-manager
  agent-version: "1"
---

# Record the Declines

## What happens

Every request not committed, with its reason.

## Where it happens

- `ref/mkt/prioritize-initiatives`, activity 13 -
  [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

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
