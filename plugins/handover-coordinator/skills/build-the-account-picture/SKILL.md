---
name: build-the-account-picture
description: Gathers everything the sale produced into one place with a date on each item, writes the account picture with a source behind every claim in it, lists every promise made along the way with who made it and to whom, and maps who decides, who pays and who uses it every day. Use it when running `ref/sls/hand-over-to-delivery`.
license: CC-BY-4.0
metadata:
  agent: handover-coordinator
  agent-version: "1"
---

# Build the account picture

## What it does

Gathers everything the sale produced into one place with a date on each
item, writes the account picture with a source behind every claim in it,
lists every promise made along the way with who made it and to whom, and
maps who decides, who pays and who uses it every day.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Collect What the Sale Learned**
  - `ref/sls/hand-over-to-delivery`, activity 3 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Map Who Is Who at the Customer**
  - `ref/sls/hand-over-to-delivery`, activity 7 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Record What Was Promised**
  - `ref/sls/hand-over-to-delivery`, activity 5 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Write the Account Picture**
  - `ref/sls/hand-over-to-delivery`, activity 4 -
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
