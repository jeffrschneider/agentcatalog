---
name: score-cases-against-the-rubric
description: Scores each case on each part of the rubric with the moment in the case behind each score and marks each score it is unsure of, scores the shared cases and the second set alone as one reviewer among the rest, and scores the part a specialist practises on their next cases. Use it when running `ref/sup/calibrate-case-reviews`, `ref/sup/coach-a-support-person` and `ref/sup/review-support-cases`.
license: CC-BY-4.0
metadata:
  agent: case-reviewer
  agent-version: "1"
---

# Score cases against the rubric

## What it does

Scores each case on each part of the rubric with the moment in the case
behind each score and marks each score it is unsure of, scores the
shared cases and the second set alone as one reviewer among the rest,
and scores the part a specialist practises on their next cases.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Agreement Held**
  - `ref/sup/calibrate-case-reviews`, activity 17 -
    [Calibrate Case Reviews](../../../../processes/customer-support/calibrate-case-reviews.md)
- **Score Each Case Against the Rubric**
  - `ref/sup/review-support-cases`, activity 5 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)
- **Score the Cases Alone**
  - `ref/sup/calibrate-case-reviews`, activity 4 -
    [Calibrate Case Reviews](../../../../processes/customer-support/calibrate-case-reviews.md)
- **Score the Practised Part on New Cases**
  - `ref/sup/coach-a-support-person`, activity 10 -
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
