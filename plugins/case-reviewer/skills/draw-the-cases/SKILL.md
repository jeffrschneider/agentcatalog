---
name: draw-the-cases
description: Opens each review period and each calibration round with the rubric version in force, draws the cases at random at the size the statistician agent set, with names hidden for a calibration round, and keeps the cases picked for a reason apart from the random sample. Use it when running `ref/sup/calibrate-case-reviews` and `ref/sup/review-support-cases`.
license: CC-BY-4.0
metadata:
  agent: case-reviewer
  agent-version: "1"
---

# Draw the cases

## What it does

Opens each review period and each calibration round with the rubric
version in force, draws the cases at random at the size the statistician
agent set, with names hidden for a calibration round, and keeps the
cases picked for a reason apart from the random sample.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Add the Cases Picked for a Reason**
  - `ref/sup/review-support-cases`, activity 4 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)
- **Draw the Sample**
  - `ref/sup/review-support-cases`, activity 3 -
    [Review Support Cases](../../../../processes/customer-support/review-support-cases.md)
- **Draw the Shared Cases**
  - `ref/sup/calibrate-case-reviews`, activity 3 -
    [Calibrate Case Reviews](../../../../processes/customer-support/calibrate-case-reviews.md)
- **Open the Calibration Round**
  - `ref/sup/calibrate-case-reviews`, activity 1 -
    [Calibrate Case Reviews](../../../../processes/customer-support/calibrate-case-reviews.md)
- **Open the Review Period**
  - `ref/sup/review-support-cases`, activity 1 -
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
