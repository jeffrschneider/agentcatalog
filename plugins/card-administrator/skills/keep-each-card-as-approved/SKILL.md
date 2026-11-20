---
name: keep-each-card-as-approved
description: Sets each approved change in the issuer's portal exactly as approved, matches each card's status, limits and rules to its approval, and keeps the card register with every old value and its date. Use it when running `ref/fin/issue-a-company-card`.
license: CC-BY-4.0
metadata:
  agent: card-administrator
  agent-version: "1"
---

# Keep each card as approved

## What it does

Sets each approved change in the issuer's portal exactly as approved,
matches each card's status, limits and rules to its approval, and keeps
the card register with every old value and its date.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Match the Card to Its Approval**
  - `ref/fin/issue-a-company-card`, activity 13 -
    [Issue a Company Card](../../../../processes/finance/issue-a-company-card.md)
- **Record the Card in the Register**
  - `ref/fin/issue-a-company-card`, activity 14 -
    [Issue a Company Card](../../../../processes/finance/issue-a-company-card.md)
- **Set the Approved Limit in the Portal**
  - `ref/fin/issue-a-company-card`, activity 10 -
    [Issue a Company Card](../../../../processes/finance/issue-a-company-card.md)

## What to record

Each card request leaves the request with its reason, the reading
against the card policy, the approver the delegation-keeper agent named,
the limit and the rules that person set in writing, the holder's
acceptance of the terms at their versions, the order to the issuer, the
activation date, and the card in the portal matched field by field to
the register. Each freeze, close or change leaves the breach, the last
day or the approval behind it, the time it took effect and the people
told, and any spend handed to the reconciliation. Each statement period
leaves every transaction taken in, the statement checked against them,
the balance sent for payment, each request and reminder for a receipt,
each transaction's result from the expense-check agent with its approval
or decision, the personal spend and when it was repaid, and the
reconciliation with each difference explained by its evidence, its
proposed entry and the reviewer's sign-off. Nothing in the record shows
this agent setting a limit nobody approved, paying a card bill or
signing off a reconciliation it prepared.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
