---
name: keep-health-information-restricted
description: Asks only for the documents the policy and the rules allow for the kind of leave, keeps every document with health information in a file only the named people may open, and passes on from the leave record only the outcome already approved. Use it when running `ref/hr/handle-an-accommodation-request` and `ref/hr/manage-a-leave-of-absence`.
license: CC-BY-4.0
metadata:
  agent: leave-coordinator
  agent-version: "1"
---

# Keep health information restricted

## What it does

Asks only for the documents the policy and the rules allow for the kind
of leave, keeps every document with health information in a file only
the named people may open, and passes on from the leave record only the
outcome already approved.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Ask for the Documents the Leave Needs**
  - `ref/hr/manage-a-leave-of-absence`, activity 4 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Keep Health Information Restricted**
  - `ref/hr/manage-a-leave-of-absence`, activity 5 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Read the Leave Record**
  - `ref/hr/handle-an-accommodation-request`, activity 4 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)

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
