---
name: write-the-document
description: "Writes the parts nobody can reuse: the problem in the customer's own words, what is included line by line, what is deliberately not included, the price and the term from the approved quote, what happens between a yes and the work starting, and the narrative a bid is read on rather than scored on. Use it when running `ref/sls/respond-to-an-rfp` and `ref/sls/write-a-proposal`."
license: CC-BY-4.0
metadata:
  agent: proposal-writer
  agent-version: "1"
---

# Write the document

## What it does

Writes the parts nobody can reuse: the problem in the customer's own
words, what is included line by line, what is deliberately not included,
the price and the term from the approved quote, what happens between a
yes and the work starting, and the narrative a bid is read on rather
than scored on.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Write What Happens Next**
  - `ref/sls/write-a-proposal`, activity 9 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Write What Is Included**
  - `ref/sls/write-a-proposal`, activity 6 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Write What Is Not Included**
  - `ref/sls/write-a-proposal`, activity 7 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Write the Narrative**
  - `ref/sls/respond-to-an-rfp`, activity 11 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Write the Price and the Terms**
  - `ref/sls/write-a-proposal`, activity 8 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Write the Problem in Their Words**
  - `ref/sls/write-a-proposal`, activity 5 -
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
