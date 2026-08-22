---
name: take-in-the-order-and-name-the-new-owner
description: Takes the booked order in with its identifier and the opportunity every note hangs off, and records the person a decision maker names as the new owner of the relationship. Use it when running `ref/sls/hand-over-to-delivery`.
license: CC-BY-4.0
metadata:
  agent: handover-coordinator
  agent-version: "1"
---

# Take in the order and name the new owner

## What it does

Takes the booked order in with its identifier and the opportunity every
note hangs off, and records the person a decision maker names as the new
owner of the relationship. The name is a person, not a queue and not a
shared mailbox.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Name Who Now Owns the Relationship**
  - `ref/sls/hand-over-to-delivery`, activity 2 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Take in the Booked Order**
  - `ref/sls/hand-over-to-delivery`, activity 1 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)

## What to record

Per handover: the order as taken in, with its identifier and the
opportunity every note hangs off. Everything the sale produced, in one
place, with a date on each item. The account picture with the source
behind every claim in it. The promise list, one per line, with who made
each promise, when, and to whom. The people, their roles, who blocked
the deal, and how each one is reached. The package scored against the
checklist at a version, naming what is missing. The internal handover
with the questions the package did not answer and the answers the seller
gave. Who says what to the customer, on what date, through which
channel. The customer's confirmation, dated, with what they were told.
What the seller still owes, each item with a date, and what the new
owner now holds.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
