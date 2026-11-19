---
name: record-what-people-decide
description: Records the final ratings the calibration panel agreed and the promotion panel's decisions with their reasons and dissent, the employee's response to the review, the next period's objectives the manager and the employee agreed, and the feedback given to each nominee not promoted. Use it when running `ref/hr/decide-promotions` and `ref/hr/run-the-performance-review`.
license: CC-BY-4.0
metadata:
  agent: performance-review-coordinator
  agent-version: "1"
---

# Record what people decide

## What it does

Records the final ratings the calibration panel agreed and the promotion
panel's decisions with their reasons and dissent, the employee's
response to the review, the next period's objectives the manager and the
employee agreed, and the feedback given to each nominee not promoted.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Next Period's Objectives**
  - `ref/hr/run-the-performance-review`, activity 14 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)
- **Give Feedback to Those Not Promoted**
  - `ref/hr/decide-promotions`, activity 14 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Record the Decisions**
  - `ref/hr/decide-promotions`, activity 11 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Record the Employee's Response**
  - `ref/hr/run-the-performance-review`, activity 13 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)
- **Record the Final Ratings**
  - `ref/hr/run-the-performance-review`, activity 10 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)

## What to record

Each review cycle leaves the people in it, the period, the date for each
step, the rating scale and the form at a version, each self-review and
each piece of peer feedback with the date it arrived or the record that
it did not, the evidence each manager received, each draft with every
flag the check raised and how the manager settled it, the calibration
packs with nothing in them about pay, health, a leave's reason, a case
or a protected characteristic, the final ratings as the panel agreed
them with the reason for any change and any dissent, the date each
review was shared, the employee's comments, the next period's
objectives, and the ratings and named promotions handed on at their
versions. Each promotion round leaves the dates, the budget, the panel
and the level expectations at a version, each nomination, each case with
its flags, the panel pack, each decision with its reasons and dissent,
the feedback each nominee not promoted received, each promotion handed
on, and the spend against the budget. Each improvement plan leaves the
record of the work it gathered and the written gap with every flag
settled before any plan was drafted. Nothing in the record shows this
agent proposing, changing or ranking a rating, or deciding a promotion
or the outcome of a plan.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
