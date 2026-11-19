---
name: take-in-the-request
description: Takes in a leave request in any form, or an absence that has passed the policy's point, acknowledges it in writing with the next step and the rights that apply, checks it against the policy and the local leave rules, and takes in time away decided on an accommodation request as a leave request with that decision beside it. Use it when running `ref/hr/handle-an-accommodation-request` and `ref/hr/manage-a-leave-of-absence`.
license: CC-BY-4.0
metadata:
  agent: leave-coordinator
  agent-version: "1"
---

# Take in the request

## What it does

Takes in a leave request in any form, or an absence that has passed the
policy's point, acknowledges it in writing with the next step and the
rights that apply, checks it against the policy and the local leave
rules, and takes in time away decided on an accommodation request as a
leave request with that decision beside it.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Acknowledge the Request**
  - `ref/hr/manage-a-leave-of-absence`, activity 2 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Check the Request Against the Rules**
  - `ref/hr/manage-a-leave-of-absence`, activity 3 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Hand Time Away to the Leave Process**
  - `ref/hr/handle-an-accommodation-request`, activity 12 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)
- **Take in the Request**
  - `ref/hr/manage-a-leave-of-absence`, activity 1 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)

## What to record

Each leave leaves the request as it arrived and how the employee asked,
the acknowledgment with its date and the rights it set out, the check
against the policy and the local rules with the leave already taken and
the leave available, each document asked for with its date and what
arrived, and the restricted file with its log of every opening. Beside
them sit the approver's decision and the written notice the employee
received, the dates the manager was told and when, each contact during
the leave kept to what the employee agreed, each extension or early
return checked and decided like the first, the return plan, and the
close with the dates taken and the balance left. For an accommodation
request it leaves the approved outcome it passed on, the time away taken
in as a leave request with the decision beside it, and the return date
kept. Nothing in the record outside the restricted file says why a leave
was taken, and nothing shows this agent deciding a leave.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
