---
name: take-in-an-ask-and-hold-its-clock
description: Takes the discount ask, checks it carries its lines, its reason and its evidence, and starts a clock the seller can see. Use it when running `ref/rev/approve-a-discount`.
license: CC-BY-4.0
metadata:
  agent: discount-approver
  agent-version: "1"
---

# Take in an ask and hold its clock

## What it does

Takes the discount ask, checks it carries its lines, its reason and its
evidence, and starts a clock the seller can see. An ask that outruns the
time its band promised goes up the line with what it waits on rather
than sitting.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Ask Is Complete**
  - `ref/rev/approve-a-discount`, activity 2 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Escalate a Clock That Ran Out**
  - `ref/rev/approve-a-discount`, activity 12 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Start the Clock**
  - `ref/rev/approve-a-discount`, activity 3 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Take in the Discount Ask**
  - `ref/rev/approve-a-discount`, activity 1 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)

## What to record

Per ask: the ask as the seller wrote it against a quote version, the
band it matched on the table at the version in force, the signer and the
delegate that band names, and the hour the clock started. Every line at
its list price with the card version it was read from and the discount
as a number. The margin at the asked price, with every line below the
floor named. The evidence the seller supplied, what this customer, this
segment and this product already got with the deals and dates it was
given on, and what the discount does to the renewal price and to the
next deal that cites it. Then the decision: the number approved, the
reason in the signer's own words, the signer, the band, and the version
of the quote it was decided against, with the quote rebuilt on the
approved number rather than the asked one. Every escalation carries what
the ask was waiting on when the clock ran out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
