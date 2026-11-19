---
name: chase-completion
description: Reminds each person before the due date, chases anyone overdue, first the person and then the manager, chases what a new hire still has open beside the policy-keeper agent, and raises anyone who stays overdue to the department head, who decides what follows. Use it when running `ref/hr/run-new-hire-orientation` and `ref/hr/run-required-training`.
license: CC-BY-4.0
metadata:
  agent: training-coordinator
  agent-version: "1"
---

# Chase completion

## What it does

Reminds each person before the due date, chases anyone overdue, first
the person and then the manager, chases what a new hire still has open
beside the policy-keeper agent, and raises anyone who stays overdue to
the department head, who decides what follows.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Chase Overdue Training**
  - `ref/hr/run-required-training`, activity 11 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)
- **Chase What Is Missing**
  - `ref/hr/run-new-hire-orientation`, activity 13 -
    [Run New Hire Orientation](../../../../processes/human-resources/run-new-hire-orientation.md)
- **Raise What Stays Overdue**
  - `ref/hr/run-required-training`, activity 12 -
    [Run Required Training](../../../../processes/human-resources/run-required-training.md)
- **Remind Before the Due Date**
  - `ref/hr/run-required-training`, activity 9 -
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
