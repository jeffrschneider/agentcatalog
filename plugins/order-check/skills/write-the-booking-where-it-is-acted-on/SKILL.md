---
name: write-the-booking-where-it-is-acted-on
description: Writes the approved booking into the order system, passes the billing schedule, the payment terms and the purchase order reference to finance, and closes the opportunity at the amount actually booked rather than the amount forecast. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: order-check
  agent-version: "1"
---

# Write the booking where it is acted on

## What it does

Writes the approved booking into the order system, passes the billing
schedule, the payment terms and the purchase order reference to finance,
and closes the opportunity at the amount actually booked rather than the
amount forecast.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Close the Opportunity**
  - `ref/sls/book-the-order`, activity 14 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Pass the Billing Terms to Finance**
  - `ref/sls/book-the-order`, activity 13 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Record the Booking**
  - `ref/sls/book-the-order`, activity 12 -
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
