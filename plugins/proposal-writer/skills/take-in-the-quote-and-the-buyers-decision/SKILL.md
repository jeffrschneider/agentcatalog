---
name: take-in-the-quote-and-the-buyers-decision
description: Starts from the approved quote as it is handed on, with its price and the date it stops holding. Use it when running `ref/sls/configure-and-price` and `ref/sls/write-a-proposal`.
license: CC-BY-4.0
metadata:
  agent: proposal-writer
  agent-version: "1"
---

# Take in the quote and the buyers decision

## What it does

Starts from the approved quote as it is handed on, with its price and
the date it stops holding. Reads how the buyer decides: who signs, who
can stop it, and what each of them needs to see.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Hand the Quote On**
  - `ref/sls/configure-and-price`, activity 13 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Read the Buyer's Decision**
  - `ref/sls/write-a-proposal`, activity 2 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Take in the Approved Quote**
  - `ref/sls/write-a-proposal`, activity 1 -
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
