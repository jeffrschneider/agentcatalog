---
name: price-the-ask-against-the-card-and-the-floor
description: Re-prices every line against the rate card at a named version, so the discount is measured off a real list price and never off a previous quote. Use it when running `ref/rev/approve-a-discount`.
license: CC-BY-4.0
metadata:
  agent: discount-approver
  agent-version: "1"
---

# Price the ask against the card and the floor

## What it does

Re-prices every line against the rate card at a named version, so the
discount is measured off a real list price and never off a previous
quote. Sets the discounted deal against the margin floor and names every
line that falls below it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Margin Against the Floor**
  - `ref/rev/approve-a-discount`, activity 6 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Check the Price as Asked**
  - `ref/rev/approve-a-discount`, activity 5 -
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
