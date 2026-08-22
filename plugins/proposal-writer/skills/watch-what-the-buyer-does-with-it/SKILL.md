---
name: watch-what-the-buyer-does-with-it
description: Watches whether the document was opened, shared and read to the end, or not at all, and answers the follow-ups and the presentation the buyer asks for after it lands. Use it when running `ref/sls/respond-to-an-rfp` and `ref/sls/write-a-proposal`.
license: CC-BY-4.0
metadata:
  agent: proposal-writer
  agent-version: "1"
---

# Watch what the buyer does with it

## What it does

Watches whether the document was opened, shared and read to the end, or
not at all, and answers the follow-ups and the presentation the buyer
asks for after it lands.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Handle Clarifications**
  - `ref/sls/respond-to-an-rfp`, activity 16 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Watch What the Buyer Does**
  - `ref/sls/write-a-proposal`, activity 14 -
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
