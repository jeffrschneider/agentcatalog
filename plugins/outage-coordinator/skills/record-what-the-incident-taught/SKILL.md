---
name: record-what-the-incident-taught
description: Records the time from the first case to the page, the first update and the summary, the cadences missed, the corrections, the notices sent late and whether the threshold was right. Use it when running `ref/sup/follow-up-an-outage`, `ref/sup/post-a-status-update` and `ref/sup/raise-a-suspected-outage`.
license: CC-BY-4.0
metadata:
  agent: outage-coordinator
  agent-version: "1"
---

# Record what the incident taught

## What it does

Records the time from the first case to the page, the first update and
the summary, the cadences missed, the corrections, the notices sent late
and whether the threshold was right.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Record What Support Learned**
  - `ref/sup/follow-up-an-outage`, activity 16 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Record What the Run Taught**
  - `ref/sup/post-a-status-update`, activity 16 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
  - `ref/sup/raise-a-suspected-outage`, activity 15 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)

## What to record

Each suspected outage leaves the signal that raised it and the time the
symptom was first seen, any incident already open and any known cause
read as a lead, every case grouped with its channel, its account and its
time, the symptom as set out in the customers' own words, the accounts
reporting it, the page with its time and the evidence it carried, the
head of support told, and the engineer's ruling, with the cases handed
on or sent back with the reason. Each status record leaves the
incident's severity, cadence and approver, each fact the incident lead
confirmed with the time, each draft at its version, any line set against
Marketing's statement, the approver's decision, exactly what was posted
and when with the time of the next update, each correction beside the
version it corrects, and each cadence kept or missed. Each incident's
customer side leaves the accounts added to engineering's list, the lists
sent to the account owners, each approved version sent to each open
linked case, each new case joined, and every affected account set
against the route it was owed. Each follow-up leaves engineering's
review as taken in, the summary at each version with each sentence's
place in the review, the approved version sent and to whom, and each
linked case closed or kept open with its reason. Nothing in the record
shows this agent confirming or ruling out an incident, posting or
sending words a named person had not approved, naming a cause, a fault
or a date the incident lead had not confirmed, or replying to a public
post.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
