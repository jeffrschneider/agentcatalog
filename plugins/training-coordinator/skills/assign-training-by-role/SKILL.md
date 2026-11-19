---
name: assign-training-by-role
description: Takes in each requirement as the learning lead confirms it, reads who it covers by role and location alone, counts what falls due in the year, and assigns each person the course at its signed version with a due date. Use it when running `ref/hr/plan-the-learning-program` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: training-coordinator
  agent-version: "1"
---

# Assign training by role

## What it does

Takes in each requirement as the learning lead confirms it, reads who it
covers by role and location alone, counts what falls due in the year,
and assigns each person the course at its signed version with a due
date. It records an exemption only on a current completion of the same
version or a named person's written grant.

## Where it happens

The agent does this in seven activities across four reference processes.
Each one names the activity as that process words it.

- **Assign the First Required Training**
  - `ref/hr/run-new-hire-orientation`, activity 6 -
    [Run New Hire Orientation](../../../../processes/human-resources/run-new-hire-orientation.md)
- **Assign the Training**
  - `ref/hr/run-required-training`, activity 6 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)
- **Assign the Training It Needs**
  - `ref/hr/publish-an-hr-policy`, activity 11 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Count the Required Training**
  - `ref/hr/plan-the-learning-program`, activity 3 -
    [Plan the Learning Program](../../../../processes/human-resources/plan-the-learning-program.md)
- **Read Who It Applies To**
  - `ref/hr/run-required-training`, activity 2 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)
- **Record Exemptions**
  - `ref/hr/run-required-training`, activity 8 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)
- **Take In the Requirement**
  - `ref/hr/run-required-training`, activity 1 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)

## What to record

Each round leaves the requirement with the rule or policy behind it, the
roles and locations it covers and its due date as the learning lead
confirmed them, the people it covers as read by role and location, each
assignment with the course version and the due date, each session
booked, and each exemption with the completion it rests on or the named
person who granted it in writing. It leaves each reminder and each chase
with its date and whom it reached, each completion with the person, the
course version, the date and any result, the people raised to the
department head with the decision recorded beside them, and the
completion report by team and location. Orientation leaves the first
courses assigned to each new hire, who attended each part of the
session, who did not and who joined late, and each course still open
passed on with its due date. A policy change leaves the training it
called for, assigned by role and location. A learning round leaves the
required training counted for the year by role and location, and the
sessions on the calendar. The record of each person, course and version
is kept for the period `<your jurisdiction's rule on keeping training
records>` sets. Nothing in the record shows this agent deciding anything
about a person who is overdue.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
