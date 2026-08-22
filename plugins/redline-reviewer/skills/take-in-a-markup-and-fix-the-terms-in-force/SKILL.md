---
name: take-in-a-markup-and-fix-the-terms-in-force
description: Takes in the buyer's markup at its version and the copy it was made from, fixes which template version and which pre-approved fallbacks are in force, and splits the document into one item per changed clause with both texts side by side. Use it when running `ref/sls/review-the-redlines`.
license: CC-BY-4.0
metadata:
  agent: redline-reviewer
  agent-version: "1"
---

# Take in a markup and fix the terms in force

## What it does

Takes in the buyer's markup at its version and the copy it was made
from, fixes which template version and which pre-approved fallbacks are
in force, and splits the document into one item per changed clause with
both texts side by side.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Confirm the Terms in Force**
  - `ref/sls/review-the-redlines`, activity 2 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Split the Markup into Clauses**
  - `ref/sls/review-the-redlines`, activity 3 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Take in the Buyer's Markup**
  - `ref/sls/review-the-redlines`, activity 1 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)

## What to record

Per review: the markup at its version and the copy it was made from. One
item per changed clause, with the original text and the buyer's text
side by side, its class, and its clause number. What was decided on the
same change in past deals and who decided it. Every clause closed as
accept, counter or reject, each with its reason and the person who made
the decision. The counter-markup with every off-template term listed
separately and every approver named. The version sent back and the date.
Each further markup read against the copy we last sent, with every
difference named. The confirmed clean text, and the accepted changes
written to the record other deals read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
