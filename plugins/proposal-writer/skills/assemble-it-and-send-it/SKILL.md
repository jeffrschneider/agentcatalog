---
name: assemble-it-and-send-it
description: Assembles one file at one version, delivers it the way the buyer asked and inside the deadline a bid sets, and records the version that actually went out with its date, its signers and its recipients. Use it when running `ref/sls/respond-to-an-rfp` and `ref/sls/write-a-proposal`.
license: CC-BY-4.0
metadata:
  agent: proposal-writer
  agent-version: "1"
---

# Assemble it and send it

## What it does

Assembles one file at one version, delivers it the way the buyer asked
and inside the deadline a bid sets, and records the version that
actually went out with its date, its signers and its recipients.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Assemble and Submit**
  - `ref/sls/respond-to-an-rfp`, activity 14 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Assemble and Version the Document**
  - `ref/sls/write-a-proposal`, activity 12 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Deliver It to the Buyer**
  - `ref/sls/write-a-proposal`, activity 13 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Record What Was Sent**
  - `ref/sls/write-a-proposal`, activity 15 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)

## What to record

Per proposal: the section list agreed at the briefing and the promised
date, every reusable section with the library version it came from and
every section the library did not have, the customer's own words with
the conversation and date each quote came from, the scope traced line by
line to the configuration that was priced, the exclusions, the price and
the date the offer stops holding, the sign-off against a named version
with the signers, and the version that actually went out with its date
and its recipients. When the buyer quotes back a price, the recorded
version settles it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
