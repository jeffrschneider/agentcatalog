---
name: check-for-examples
description: Reads each manager's draft review, each promotion case and each written gap for an example of the work behind every rating, expectation or point, and flags every remark about personality with its line named, leaving the words and the judgment to the manager. Use it when running `ref/hr/decide-promotions`, `ref/hr/run-a-performance-improvement-plan` and `ref/hr/run-the-performance-review`.
license: CC-BY-4.0
metadata:
  agent: performance-review-coordinator
  agent-version: "1"
---

# Check for examples

## What it does

Reads each manager's draft review, each promotion case and each written
gap for an example of the work behind every rating, expectation or
point, and flags every remark about personality with its line named,
leaving the words and the judgment to the manager.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check Each Case for Evidence**
  - `ref/hr/decide-promotions`, activity 4 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Check Each Draft for Evidence**
  - `ref/hr/run-the-performance-review`, activity 6 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)
- **Check the Written Gap for Evidence**
  - `ref/hr/run-a-performance-improvement-plan`, activity 5 -
    [Run a Performance Improvement Plan](../../../../processes/human-resources/run-a-performance-improvement-plan.md)

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
