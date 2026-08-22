---
name: check-the-handover-package
description: Takes the booked order in and scores the handover package against its checklist at a version, naming what is missing rather than what is present. Use it when running `ref/sls/hand-over-to-delivery`.
license: CC-BY-4.0
metadata:
  agent: order-check
  agent-version: "1"
---

# Check the handover package

## What it does

Takes the booked order in and scores the handover package against its
checklist at a version, naming what is missing rather than what is
present. A gap is carried forward with a date rather than waived
quietly.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Package Is Complete**
  - `ref/sls/hand-over-to-delivery`, activity 9 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Take in the Booked Order**
  - `ref/sls/hand-over-to-delivery`, activity 1 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)

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
