---
name: keep-the-development-plans
description: Writes into each employee's development plan the actions chosen at a review, the actions each successor agreed, the feedback an internal applicant who was not chosen agreed to keep, and the plan a mover writes again for the new role, each with an owner and a date. Use it when running `ref/hr/move-an-employee-to-a-new-role`, `ref/hr/plan-succession-for-key-roles` and `ref/hr/run-the-performance-review`.
license: CC-BY-4.0
metadata:
  agent: career-planner
  agent-version: "1"
---

# Keep the development plans

## What it does

Writes into each employee's development plan the actions chosen at a
review, the actions each successor agreed, the feedback an internal
applicant who was not chosen agreed to keep, and the plan a mover writes
again for the new role, each with an owner and a date.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Add Development Actions**
  - `ref/hr/plan-succession-for-key-roles`, activity 12 -
    [Plan Succession for Key Roles](../../../../processes/human-resources/plan-succession-for-key-roles.md)
- **Record Feedback in the Development Plan**
  - `ref/hr/move-an-employee-to-a-new-role`, activity 9 -
    [Move an Employee to a New Role](../../../../processes/human-resources/move-an-employee-to-a-new-role.md)
- **Record the Development Plan**
  - `ref/hr/run-the-performance-review`, activity 15 -
    [Run the Performance Review](../../../../processes/human-resources/run-the-performance-review.md)
- **Reset the Development Plan**
  - `ref/hr/move-an-employee-to-a-new-role`, activity 16 -
    [Move an Employee to a New Role](../../../../processes/human-resources/move-an-employee-to-a-new-role.md)

## What to record

Each development plan leaves its actions at a version, each with an
owner, a date and the support the company gives, and the source of each
action: a review conversation, a succession review, or an internal
application the person was not chosen for. Each succession review leaves
the request to each manager with the role's needs and the readiness
scale, each readiness view with the evidence behind it as the manager
recorded it, each view that had no evidence named and sent back, each
person's stated interest beside the roles they were named for, and the
pack as it went to the leaders, with no pay, health, leave, case record
or protected characteristic in it. It leaves each role with no ready
successor, each development need a readiness view waits on, and each
successor's actions as the person and the manager agreed them. A
learning round leaves the needs counted by skill and by team with no
person named, and the people told that a course is there or that their
need was left out, with the reason. A move leaves the employees told of
the opening, the feedback each applicant who was not chosen agreed to
keep, and the mover's plan written again for the new role. Nothing in
the record shows this agent naming, ranking or scoring a successor or an
applicant.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
