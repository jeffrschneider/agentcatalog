---
name: test-the-booking-against-the-record
description: Prices every line at a price book version or names the approval that let it differ, matches every sold line to something that exists and to a date the delivery side can meet, and scores the whole booking against the booking rules at a version. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: order-check
  agent-version: "1"
---

# Test the booking against the record

## What it does

Prices every line at a price book version or names the approval that let
it differ, matches every sold line to something that exists and to a
date the delivery side can meet, and scores the whole booking against
the booking rules at a version. A booking that fails goes back to be
corrected.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check What Was Sold Against What Exists**
  - `ref/sls/book-the-order`, activity 8 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Price the Booking**
  - `ref/sls/book-the-order`, activity 6 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Score the Booking**
  - `ref/sls/book-the-order`, activity 10 -
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
