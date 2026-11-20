---
name: raise-what-the-cases-show
description: Raises the same day any case that shows a missed approval, a skipped identity check or exposed data, and sends each score that traces to an article, a saved reply or a routing rule to the owner of the fix. Use it when running `ref/sup/review-support-cases`.
license: CC-BY-4.0
metadata:
  agent: case-reviewer
  agent-version: "1"
---

# Raise what the cases show

## What it does

Raises the same day any case that shows a missed approval, a skipped
identity check or exposed data, and sends each score that traces to an
article, a saved reply or a routing rule to the owner of the fix.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Raise What Cannot Wait**
  - `ref/sup/review-support-cases`, activity 6 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)
- **Send Desk Faults to Their Owners**
  - `ref/sup/review-support-cases`, activity 11 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)

## What to record

Each review period leaves the population, the sample size set before the
draw and the draw itself, so that anyone can draw it again, the cases
picked for a reason kept apart, each score with the rubric version and
the moment behind it, each score marked uncertain and how a reviewer
settled it, each case raised the same day and what the quality lead
decided, each desk fault with its owner, the results as sent and to
whom, each disputed score with the first score kept and the second
reading beside it, and the cases handed to coaching. Each calibration
round leaves the shared cases with names hidden, every reviewer's scores
given alone with this agent's own among them, each split with the
moments cited, the agreed readings with their examples at the rubric
version, and each reviewer's own scores as sent. Each coaching cycle
leaves the cases prepared, any score sent for a second reading in the
specialist's own words, and the practised part scored on the next cases.
Nothing in the record shows this agent ranking or rating a specialist,
changing a score after seeing another reviewer's, or sending a
specialist's results to anyone but that specialist and their team lead.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
