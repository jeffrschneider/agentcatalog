---
name: plan-how-the-day-runs
description: The agent works out the footprint, who is where, and what happens minute by minute, then runs the rehearsal that tests whether the plan holds. Use it when running `ref/mkt/field-event` and `ref/mkt/trade-show`.
license: CC-BY-4.0
metadata:
  agent: event-operations
  agent-version: "1"
---

# Plan how the day runs

## What it does

The agent works out the footprint, who is where, and what happens minute
by minute, then runs the rehearsal that tests whether the plan holds.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Plan the Presence**
  - `ref/mkt/trade-show`, activity 3 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Prepare the Run of Show**
  - `ref/mkt/field-event`, activity 11 -
    [Host Field Event](../../../../processes/marketing/field-event.md)

## What to record

Every rule it read lands with where it came from and the date it was
published, together with the calendar of deadlines it turned those rules
into. Every quote is kept at the price and the terms quoted, with the
date the quote expires. Every order says what was ordered, from whom, at
what price, when it is due, and the date it must be cancelled by to
avoid a charge. A dated record says what shipped, when it shipped, when
it arrived, and what was missing. The load-in and the teardown are
written down as they actually happened, including what was damaged, lost
or returned. The cost of the event is left line by line beside what was
ordered.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
