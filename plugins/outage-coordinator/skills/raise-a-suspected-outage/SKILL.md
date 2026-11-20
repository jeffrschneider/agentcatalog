---
name: raise-a-suspected-outage
description: Opens one suspected outage for a symptom, reads whether an incident is already open and what known cause may match, groups the cases, sets out the symptom in the customers' words, lists the accounts reporting it, pages the engineer on call with the evidence, and hands on or sends back the cases once the engineer rules. Use it when running `ref/sup/raise-a-suspected-outage`.
license: CC-BY-4.0
metadata:
  agent: outage-coordinator
  agent-version: "1"
---

# Raise a suspected outage

## What it does

Opens one suspected outage for a symptom, reads whether an incident is
already open and what known cause may match, groups the cases, sets out
the symptom in the customers' words, lists the accounts reporting it,
pages the engineer on call with the evidence, and hands on or sends back
the cases once the engineer rules.

## Where it happens

The agent does this in nine activities across one reference process.
Each one names the activity as that process words it.

- **Check for a Known Cause**
  - `ref/sup/raise-a-suspected-outage`, activity 5 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Check for an Incident Already Open**
  - `ref/sup/raise-a-suspected-outage`, activity 4 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Group the Cases**
  - `ref/sup/raise-a-suspected-outage`, activity 7 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Hand On a Confirmed Incident**
  - `ref/sup/raise-a-suspected-outage`, activity 13 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **List the Accounts Reporting It**
  - `ref/sup/raise-a-suspected-outage`, activity 9 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Open the Suspected Outage**
  - `ref/sup/raise-a-suspected-outage`, activity 3 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Page the Engineer on Call**
  - `ref/sup/raise-a-suspected-outage`, activity 10 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Send Back a Ruled-Out Alarm**
  - `ref/sup/raise-a-suspected-outage`, activity 14 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Set Out the Symptom**
  - `ref/sup/raise-a-suspected-outage`, activity 8 -
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
