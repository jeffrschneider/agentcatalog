---
name: hand-on-and-close
description: Hands the final ratings to the pay review and each promotion on to the record, and closes each cycle and round with what finished on time, what was sent back and why, and what the next one does differently. Use it when running `ref/hr/decide-promotions` and `ref/hr/run-the-performance-review`.
license: CC-BY-4.0
metadata:
  agent: performance-review-coordinator
  agent-version: "1"
---

# Hand on and close

## What it does

Hands the final ratings to the pay review and each promotion on to the
record, and closes each cycle and round with what finished on time, what
was sent back and why, and what the next one does differently.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Close the Cycle on the Record**
  - `ref/hr/run-the-performance-review`, activity 17 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)
- **Close the Round on the Record**
  - `ref/hr/decide-promotions`, activity 17 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Hand On Each Promotion**
  - `ref/hr/decide-promotions`, activity 16 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Hand On the Ratings**
  - `ref/hr/run-the-performance-review`, activity 16 -
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
