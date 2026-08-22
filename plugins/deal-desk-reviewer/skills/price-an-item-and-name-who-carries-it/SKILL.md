---
name: price-an-item-and-name-who-carries-it
description: Says what each item risks in revenue, margin, delivery and precedent, with the number behind the risk wherever there is one, and names the person or function that carries it. Use it when running `ref/rev/review-a-non-standard-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-desk-reviewer
  agent-version: "1"
---

# Price an item and name who carries it

## What it does

Says what each item risks in revenue, margin, delivery and precedent,
with the number behind the risk wherever there is one, and names the
person or function that carries it. Looks up what was decided the last
time the same thing was asked and what happened to that deal afterwards.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Look Up the Precedent**
  - `ref/rev/review-a-non-standard-deal`, activity 10 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)
- **Price What Each Item Risks**
  - `ref/rev/review-a-non-standard-deal`, activity 7 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)
- **Say Who Carries Each Risk**
  - `ref/rev/review-a-non-standard-deal`, activity 8 -
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
