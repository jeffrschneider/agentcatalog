---
name: gather-what-the-decision-needs
description: Books the conversation between the employee, the manager and the HR business partner, collects only the information the decision needs about the limit on the work, and lists each option with its cost, its time and its effect on the work. Use it when running `ref/hr/handle-an-accommodation-request`.
license: CC-BY-4.0
metadata:
  agent: accommodation-coordinator
  agent-version: "1"
---

# Gather what the decision needs

## What it does

Books the conversation between the employee, the manager and the HR
business partner, collects only the information the decision needs about
the limit on the work, and lists each option with its cost, its time and
its effect on the work.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Collect Only the Information Needed**
  - `ref/hr/handle-an-accommodation-request`, activity 7 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)
- **List the Options**
  - `ref/hr/handle-an-accommodation-request`, activity 8 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)
- **Set Up the Conversation**
  - `ref/hr/handle-an-accommodation-request`, activity 5 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)

## What to record

Each request leaves the request as it came, with the date, the job and
what the employee asked for, and any health detail the employee offered
held in the restricted file alone. It leaves the acknowledgment with
what happens next, who will see what and the date a decision is due, the
restricted file with every opening logged, the conversation booked with
who attended and what was shared, and the information asked for under
`<your jurisdiction's rules on health information at work>` with what
was given. It leaves each option with its cost, its time and its effect
on the work, the decision with its reasons and the named person who made
it, the date the change was put in place and what each team was told,
and each review with whether the change still works for the employee and
for the work. The request closes with the change kept and its next
review date, or ended, and with the date its file is to be destroyed
under `<your records retention schedule>`. The debrief names no
employee. Nothing in the record shows this agent deciding a request, or
using the reason for it in anything else about the employee.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
