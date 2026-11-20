---
name: work-out-what-is-owed
description: Sets each request against the refund policy and any right a local rule gives, and reads each agreement against the downtime measured after an outage for the credit it owes. Use it when running `ref/sup/decide-a-refund-request` and `ref/sup/follow-up-an-outage`.
license: CC-BY-4.0
metadata:
  agent: refund-coordinator
  agent-version: "1"
---

# Work out what is owed

## What it does

Sets each request against the refund policy and any right a local rule
gives, and reads each agreement against the downtime measured after an
outage for the credit it owes.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set the Request Against the Policy**
  - `ref/sup/decide-a-refund-request`, activity 3 -
    [Decide a Refund Request](../../../../processes/customer-support/decide-a-refund-request.md)
- **Work Out the Credits Owed**
  - `ref/sup/follow-up-an-outage`, activity 10 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)

## What to record

Each refund leaves the request in the customer's own words, the order,
the invoice and the payment as read with where each was read, the
reading against the refund policy and any local rule with the rule that
applies, what the account already received, what the support specialist
said, the proposal at its version with the names of everyone who
proposed it, the decider and the decision with its reason, the credit
note, the item passed to Finance's payment run, and the reply as sent.
Each goodwill credit leaves who asked, the failure with its dates and
what the customer bore, what the agreement already owed, what the
account owner said, the proposal, the decision and its decider, the
credit note and the offer as sent, or the refusal with its reason told
to the person who asked. Each outage leaves, for each affected account,
the agreement's clause, the downtime measured, the credit worked out,
the proposal, the decision and what was passed to Finance. Nothing in
the record shows this agent deciding a refund or a credit, issuing a
credit note, moving money, or telling a customer about an amount that no
named person has decided.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
