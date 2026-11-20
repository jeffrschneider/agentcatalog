---
name: tell-the-affected-accounts
description: Opens the customer side of the incident, adds the accounts behind the linked cases, sends each account owner their affected accounts, sends each approved version to every open linked case and the approved summary to every affected account, joins each new case to the incident, and confirms that every account was told by the route it was owed. Use it when running `ref/sup/follow-up-an-outage` and `ref/sup/tell-affected-customers`.
license: CC-BY-4.0
metadata:
  agent: outage-coordinator
  agent-version: "1"
---

# Tell the affected accounts

## What it does

Opens the customer side of the incident, adds the accounts behind the
linked cases, sends each account owner their affected accounts, sends
each approved version to every open linked case and the approved summary
to every affected account, joins each new case to the incident, and
confirms that every account was told by the route it was owed.

## Where it happens

The agent does this in nine activities across two reference processes.
Each one names the activity as that process words it.

- **Add the Accounts Behind Linked Cases**
  - `ref/sup/tell-affected-customers`, activity 3 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Confirm Who Has Been Told**
  - `ref/sup/tell-affected-customers`, activity 14 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Join Each New Case to the Incident**
  - `ref/sup/tell-affected-customers`, activity 9 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Open the Customer Side of the Incident**
  - `ref/sup/tell-affected-customers`, activity 1 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send Each Later Update**
  - `ref/sup/tell-affected-customers`, activity 12 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send the Account Owners Their Accounts**
  - `ref/sup/tell-affected-customers`, activity 5 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send the Resolved Update**
  - `ref/sup/tell-affected-customers`, activity 13 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send the Summary**
  - `ref/sup/follow-up-an-outage`, activity 8 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Send the Update to Each Open Case**
  - `ref/sup/tell-affected-customers`, activity 6 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)

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
