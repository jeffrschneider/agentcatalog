---
name: break-down-and-ship-back
description: The agent runs the teardown and the return freight, and writes down what was kept, what was damaged and what did not come back. Use it when running `ref/mkt/trade-show`.
license: CC-BY-4.0
metadata:
  agent: event-operations
  agent-version: "1"
---

# Break down and ship back

## What it does

The agent runs the teardown and the return freight, and writes down what
was kept, what was damaged and what did not come back.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Break down the Booth**
  - `ref/mkt/trade-show`, activity 14 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)

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
