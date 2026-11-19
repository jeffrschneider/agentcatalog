---
name: track-the-leave
description: Tells the manager the dates and nothing about the reason, tracks the leave and any change tied to a return from it to their dates, checks an extension or an early return for the approver, plans the return with the manager, and closes the leave on the record with the dates taken and the balance left. Use it when running `ref/hr/handle-an-accommodation-request` and `ref/hr/manage-a-leave-of-absence`.
license: CC-BY-4.0
metadata:
  agent: leave-coordinator
  agent-version: "1"
---

# Track the leave

## What it does

Tells the manager the dates and nothing about the reason, tracks the
leave and any change tied to a return from it to their dates, checks an
extension or an early return for the approver, plans the return with the
manager, and closes the leave on the record with the dates taken and the
balance left.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Close the Leave on the Record**
  - `ref/hr/manage-a-leave-of-absence`, activity 18 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Decide an Extension or an Early Return**
  - `ref/hr/manage-a-leave-of-absence`, activity 14 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Plan the Return**
  - `ref/hr/manage-a-leave-of-absence`, activity 15 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Tell the Manager the Dates**
  - `ref/hr/manage-a-leave-of-absence`, activity 10 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Track the Leave**
  - `ref/hr/manage-a-leave-of-absence`, activity 13 -
    [Manage a Leave of Absence](../../../../processes/human-resources/manage-a-leave-of-absence.md)
- **Track the Return Date**
  - `ref/hr/handle-an-accommodation-request`, activity 14 -
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
