---
name: put-scores-before-a-person
description: Brings every uncertain score and every failed critical part to a reviewer, and sends a score the specialist and their team lead question back for a second reading by a reviewer who did not give it. Use it when running `ref/sup/coach-a-support-person` and `ref/sup/review-support-cases`.
license: CC-BY-4.0
metadata:
  agent: case-reviewer
  agent-version: "1"
---

# Put scores before a person

## What it does

Brings every uncertain score and every failed critical part to a
reviewer, and sends a score the specialist and their team lead question
back for a second reading by a reviewer who did not give it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Scores a Person Must Read**
  - `ref/sup/review-support-cases`, activity 7 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)
- **Send a Questioned Score Back**
  - `ref/sup/coach-a-support-person`, activity 6 -
    [Coach a Support Person](../../../../processes/customer-support/coach-a-support-person.md)

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
