---
name: keep-the-map-true-as-people-move
description: Watches for joiners, leavers and title changes, and reads the people again at review against the version the plan was built on. Use it when running `ref/sls/map-the-account-people` and `ref/sls/review-the-account-plans`.
license: CC-BY-4.0
metadata:
  agent: relationship-mapper
  agent-version: "1"
---

# Keep the map true as people move

## What it does

Watches for joiners, leavers and title changes, and reads the people
again at review against the version the plan was built on. A plan is
never left standing on a buyer who left.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check Whether the People Changed**
  - `ref/sls/review-the-account-plans`, activity 5 -
    [Review the Account Plans](../../../../processes/sales/review-the-account-plans.md)
- **Watch for People Moving**
  - `ref/sls/map-the-account-people`, activity 14 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)

## What to record

Per person: the decision they sit under, whether they decide, influence,
block or use, the source they were found in and that source's
publication date, the reporting line behind any claim of authority, the
strength score with the contact history it was computed from, the path
in and who at our end holds it, and the stance with what was said or
done behind it. Per map: every decision with no decider found or nobody
we know marked as a gap rather than left blank, what the privacy check
removed and the rule behind each removal, and the issued version naming
who corrected what and when they signed. A claim that somebody knows a
buyer well is recorded as a claim, with the person who made it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
