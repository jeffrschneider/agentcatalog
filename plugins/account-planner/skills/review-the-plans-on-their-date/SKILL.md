---
name: review-the-plans-on-their-date
description: Brings every plan in scope back up, tests what each one assumed against what actually happened, scores it, and sorts it into what happens next. Use it when running `ref/sls/review-the-account-plans`.
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Review the plans on their date

## What it does

Brings every plan in scope back up, tests what each one assumed against
what actually happened, scores it, and sorts it into what happens next.
Effort moves, plans that change are amended at a new version, plans that
stop are retired, and the readers are told.

## Where it happens

The agent does this in ten activities across one reference process. Each
one names the activity as that process words it.

- **Amend the Plans that Change**
  - `ref/sls/review-the-account-plans`, activity 11 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Move the Effort**
  - `ref/sls/review-the-account-plans`, activity 10 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Open the Review Round**
  - `ref/sls/review-the-account-plans`, activity 1 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Pull Every Plan in Scope**
  - `ref/sls/review-the-account-plans`, activity 2 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Record What the Round Taught**
  - `ref/sls/review-the-account-plans`, activity 14 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Retire the Plans that Stop**
  - `ref/sls/review-the-account-plans`, activity 12 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Score Each Plan**
  - `ref/sls/review-the-account-plans`, activity 6 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Sort the Plans into What Happens Next**
  - `ref/sls/review-the-account-plans`, activity 7 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Tell the Readers**
  - `ref/sls/review-the-account-plans`, activity 13 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Test the Assumptions Again**
  - `ref/sls/review-the-account-plans`, activity 4 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)

## What to record

The account read at a version, every line naming the system or document
it came from and the date that value was current, with the questions
nothing answered left standing as unknown. The plan at a version: each
opportunity with the evidence for it and against it, its buyer or the
note that it has none, its size in a confidence band, the order and what
each step depends on the one before it delivering, the assumptions
written as testable statements, the risks and what the plan does about
each, the moves with their owners and dates, and the asks naming who had
to agree. The signed version names both signers and the date. At review,
each plan is scored against what it said when it was signed, and every
decision records who made it, on what evidence, and anyone who
disagreed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
