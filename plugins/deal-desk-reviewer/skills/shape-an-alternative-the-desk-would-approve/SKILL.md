---
name: shape-an-alternative-the-desk-would-approve
description: Builds the version of the ask the desk would say yes to, priced beside what was asked for, and hands it back to the seller. Use it when running `ref/rev/review-a-non-standard-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-desk-reviewer
  agent-version: "1"
---

# Shape an alternative the desk would approve

## What it does

Builds the version of the ask the desk would say yes to, priced beside
what was asked for, and hands it back to the seller. A refusal is never
the only answer a seller gets.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hand the Shape Back**
  - `ref/rev/review-a-non-standard-deal`, activity 15 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)
- **Shape What the Desk Would Approve**
  - `ref/rev/review-a-non-standard-deal`, activity 11 -
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
