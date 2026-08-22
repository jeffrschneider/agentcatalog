---
name: book-the-space-and-the-suppliers
description: The agent gathers quotes and places the orders for the space, the food, the equipment, the travel and the rooms the event needs. Use it when running `ref/mkt/advisory-board` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: event-operations
  agent-version: "1"
---

# Book the space and the suppliers

## What it does

The agent gathers quotes and places the orders for the space, the food,
the equipment, the travel and the rooms the event needs. Every order is
recorded with its price, when it is due and the date it has to be
cancelled by.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Book the Venue and Suppliers**
  - `ref/mkt/field-event`, activity 3 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Book the Venue and the Suppliers**
  - `ref/mkt/user-conference`, activity 3 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Handle the Arrangements**
  - `ref/mkt/speaking-engagement`, activity 11 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)
- **Make the Arrangements**
  - `ref/mkt/advisory-board`, activity 6 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)

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
