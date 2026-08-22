---
name: test-the-ask-against-what-others-already-got
description: Reads the evidence the seller supplied and sets the ask against what this customer, this segment and this product already got, with the deals and dates it was given on. Use it when running `ref/rev/approve-a-discount`.
license: CC-BY-4.0
metadata:
  agent: discount-approver
  agent-version: "1"
---

# Test the ask against what others already got

## What it does

Reads the evidence the seller supplied and sets the ask against what
this customer, this segment and this product already got, with the deals
and dates it was given on. Writes down what the discount does to the
renewal price and to the next deal that cites it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Read the Evidence**
  - `ref/rev/approve-a-discount`, activity 7 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Say What the Discount Costs Later**
  - `ref/rev/approve-a-discount`, activity 9 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Test the Ask Against the Precedent**
  - `ref/rev/approve-a-discount`, activity 8 -
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
