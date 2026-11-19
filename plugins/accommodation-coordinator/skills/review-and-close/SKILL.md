---
name: review-and-close
description: Reviews the change on its date with the employee and the manager, closes the request with its next review date or the end of the change and the file's retention date, and adds what the request showed to the debrief with no employee named. Use it when running `ref/hr/handle-an-accommodation-request`.
license: CC-BY-4.0
metadata:
  agent: accommodation-coordinator
  agent-version: "1"
---

# Review and close

## What it does

Reviews the change on its date with the employee and the manager, closes
the request with its next review date or the end of the change and the
file's retention date, and adds what the request showed to the debrief
with no employee named.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Close the Request on the Record**
  - `ref/hr/handle-an-accommodation-request`, activity 16 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)
- **Record What the Request Taught**
  - `ref/hr/handle-an-accommodation-request`, activity 17 -
    [Handle an Accommodation Request](../../../../processes/human-resources/handle-an-accommodation-request.md)
- **Review the Change on Its Date**
  - `ref/hr/handle-an-accommodation-request`, activity 15 -
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
