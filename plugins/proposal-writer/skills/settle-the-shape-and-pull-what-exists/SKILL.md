---
name: settle-the-shape-and-pull-what-exists
description: Agrees the shape, the length and the format the buyer asked for, then pulls the sections the library already holds at their approved versions. Use it when running `ref/sls/write-a-proposal`.
license: CC-BY-4.0
metadata:
  agent: proposal-writer
  agent-version: "1"
---

# Settle the shape and pull what exists

## What it does

Agrees the shape, the length and the format the buyer asked for, then
pulls the sections the library already holds at their approved versions.
Every section the library does not have is named rather than assumed.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Agree the Shape of the Document**
  - `ref/sls/write-a-proposal`, activity 3 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Pull the Reusable Parts**
  - `ref/sls/write-a-proposal`, activity 4 -
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
