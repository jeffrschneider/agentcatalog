---
name: draft-from-confirmed-facts
description: Opens the status record, takes in what the incident lead confirmed and engineering's review, and drafts each update, correction, resolved update and summary at a version from those facts alone, set beside Marketing's statement once the press has it. Use it when running `ref/sup/follow-up-an-outage` and `ref/sup/post-a-status-update`.
license: CC-BY-4.0
metadata:
  agent: outage-coordinator
  agent-version: "1"
---

# Draft from confirmed facts

## What it does

Opens the status record, takes in what the incident lead confirmed and
engineering's review, and drafts each update, correction, resolved
update and summary at a version from those facts alone, set beside
Marketing's statement once the press has it.

## Where it happens

The agent does this in eight activities across two reference processes.
Each one names the activity as that process words it.

- **Draft a Correction**
  - `ref/sup/post-a-status-update`, activity 10 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
- **Draft the Resolved Update**
  - `ref/sup/post-a-status-update`, activity 12 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
- **Draft the Summary for Customers**
  - `ref/sup/follow-up-an-outage`, activity 5 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Draft the Update**
  - `ref/sup/post-a-status-update`, activity 3 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
- **Open the Status Record**
  - `ref/sup/post-a-status-update`, activity 1 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
- **Set the Draft Beside Marketing's Statement**
  - `ref/sup/post-a-status-update`, activity 4 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)
- **Take In Engineering's Review**
  - `ref/sup/follow-up-an-outage`, activity 4 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Take In What the Incident Lead Confirmed**
  - `ref/sup/post-a-status-update`, activity 2 -
    [Post a Status Update](../../../../processes/customer-support/post-a-status-update.md)

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
