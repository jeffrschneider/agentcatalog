---
name: close-the-sales-side-out
description: Closes out what the seller still owes, each item with a date, against what the new owner now holds. Use it when running `ref/pc/hand-over-to-the-portfolio-team` and `ref/sls/hand-over-to-delivery`.
license: CC-BY-4.0
metadata:
  agent: handover-coordinator
  agent-version: "1"
---

# Close the sales side out

## What it does

Closes out what the seller still owes, each item with a date, against
what the new owner now holds. Files what the sale should have captured
the first time, so the next handover starts from a fuller package.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Close Out the Deal Side**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 15 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Close Out the Sales Side**
  - `ref/sls/hand-over-to-delivery`, activity 15 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)
- **Record What the Handover Missed**
  - `ref/pc/hand-over-to-the-portfolio-team`, activity 16 -
    [Hand Over to the Portfolio Team](../../../../processes/private-capital/hand-over-to-the-portfolio-team.md)
- **Record What the Sale Did Not Capture**
  - `ref/sls/hand-over-to-delivery`, activity 16 -
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
