---
name: get-the-booking-approved
description: Puts the booking in front of the finance approver at a version and records who signed it and when. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: order-check
  agent-version: "1"
---

# Get the booking approved

## What it does

Puts the booking in front of the finance approver at a version and
records who signed it and when. A booking that changes afterwards goes
back through approval, because the approval covered a version.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Get Finance Approval**
  - `ref/sls/book-the-order`, activity 11 -
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
