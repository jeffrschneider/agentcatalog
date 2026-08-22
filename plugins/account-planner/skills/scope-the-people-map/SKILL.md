---
name: scope-the-people-map
description: Says which decisions the people map has to cover before anybody starts mapping, and reads the finished map back with the account team. Use it when running `ref/sls/map-the-account-people`.
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Scope the people map

## What it does

Says which decisions the people map has to cover before anybody starts
mapping, and reads the finished map back with the account team. A
decision nobody covers is named as a gap rather than left blank.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Name the Coverage Gaps**
  - `ref/sls/map-the-account-people`, activity 10 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)
- **Name the Decisions to Map**
  - `ref/sls/map-the-account-people`, activity 2 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)
- **Review the Map with the Account Team**
  - `ref/sls/map-the-account-people`, activity 12 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)
- **Take in the Account Read**
  - `ref/sls/map-the-account-people`, activity 1 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)

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
