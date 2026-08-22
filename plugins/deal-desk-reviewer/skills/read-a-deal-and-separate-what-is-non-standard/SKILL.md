---
name: read-a-deal-and-separate-what-is-non-standard
description: Reads the deal as it stands, then writes every non-standard item down on its own in the words the customer used, so each one is decided separately rather than as one document. Use it when running `ref/rev/review-a-non-standard-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-desk-reviewer
  agent-version: "1"
---

# Read a deal and separate what is non standard

## What it does

Reads the deal as it stands, then writes every non-standard item down on
its own in the words the customer used, so each one is decided
separately rather than as one document.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Name Every Non-Standard Item**
  - `ref/rev/review-a-non-standard-deal`, activity 5 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)
- **Read the Deal as It Stands**
  - `ref/rev/review-a-non-standard-deal`, activity 4 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)

## What to record

Per request: the ask as the seller wrote it, the deal it belongs to, the
level read off the published table, the time that level promises, and
the hour the seller was told both. Every non-standard item written down
on its own in the words the customer used, each carrying what it risks
with the number behind the risk wherever there is one, and the person or
function that carries it. Every read as it came back, dated, with the
reason the owner gave, and every item nobody read. What was decided the
last time the same thing was asked, on which deal, by whom, and what
happened to that deal afterwards. The alternative the desk would
approve, priced beside the ask. Then per item: the decision, the reason,
the signer, and the version of the deal it was decided against, with the
approved shape or the refusal as it went back to the seller.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
