---
name: read-the-paper-into-a-booking
description: Lifts the terms out of the executed agreement into fields, each field naming the clause it came from, and sets the start, end, notice and renewal dates against the clause that fixed each one. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: order-check
  agent-version: "1"
---

# Read the paper into a booking

## What it does

Lifts the terms out of the executed agreement into fields, each field
naming the clause it came from, and sets the start, end, notice and
renewal dates against the clause that fixed each one. A date the paper
leaves open is named as open rather than guessed.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Read the Terms into a Booking**
  - `ref/sls/book-the-order`, activity 4 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Set the Term and the Dates**
  - `ref/sls/book-the-order`, activity 5 -
    [Book the Order](../../../../processes/sales/book-the-order.md)

## What to record

Per booking: each field with the clause it was read from. The start,
end, notice and renewal dates with the clause that set each one, and any
date the paper leaves ambiguous named as ambiguous. Every line with its
catalog item, its quantity and its price at a price book version, or the
approval that let it differ. The deliverability check line by line,
naming what cannot be delivered as sold and what can be delivered
instead. The score against the booking rules at a version, with the rule
behind every failure and the written acceptance carrying any failure
forward. The approver, the date, and the version they signed. The
billing schedule as finance accepted it. The handover package scored
against its checklist version, naming what is missing rather than what
is present.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
