---
name: route-an-ask-to-the-signer-the-table-names
description: Builds the published table into the routing so an ask lands at its band, reads the band, the signer and the delegate off that table at the version in force, and puts the packet in front of the signer. Use it when running `ref/rev/approve-a-discount` and `ref/rev/publish-the-approval-thresholds`.
license: CC-BY-4.0
metadata:
  agent: discount-approver
  agent-version: "1"
---

# Route an ask to the signer the table names

## What it does

Builds the published table into the routing so an ask lands at its band,
reads the band, the signer and the delegate off that table at the
version in force, and puts the packet in front of the signer. The
decision is theirs, and the reason is recorded in their own words.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Decide, and Say Why**
  - `ref/rev/approve-a-discount`, activity 11 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Find the Level That Applies**
  - `ref/rev/approve-a-discount`, activity 4 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Route to the Signer**
  - `ref/rev/approve-a-discount`, activity 10 -
    [Approve a Discount](../../../../processes/revenue-operations/approve-a-discount.md)
- **Wire the Table Into the Routing**
  - `ref/rev/publish-the-approval-thresholds`, activity 14 -
    [Publish the Approval Thresholds](../../../../processes/revenue-operations/publish-the-approval-thresholds.md)

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
