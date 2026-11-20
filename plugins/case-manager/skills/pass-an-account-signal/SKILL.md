---
name: pass-an-account-signal
description: Writes up a sign that an account may leave or buy more in the customer's own words, sorts it with the support specialist, joins it to anything Sales already holds, confirms the account owner has it, and records where it went and what Sales decided. Use it when running `ref/sup/flag-an-account-signal`.
license: CC-BY-4.0
metadata:
  agent: case-manager
  agent-version: "1"
---

# Pass an account signal

## What it does

Writes up a sign that an account may leave or buy more in the customer's
own words, sorts it with the support specialist, joins it to anything
Sales already holds, confirms the account owner has it, and records
where it went and what Sales decided.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Check Whether Sales Already Holds It**
  - `ref/sup/flag-an-account-signal`, activity 5 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)
- **Confirm the Account Owner Has It**
  - `ref/sup/flag-an-account-signal`, activity 9 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)
- **Record Where the Signal Went**
  - `ref/sup/flag-an-account-signal`, activity 10 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)
- **Sort the Signal**
  - `ref/sup/flag-an-account-signal`, activity 4 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)
- **Take Back What Sales Decided**
  - `ref/sup/flag-an-account-signal`, activity 11 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)
- **Write Down the Customer's Own Words**
  - `ref/sup/flag-an-account-signal`, activity 2 -
    [Flag an Account Signal](../../../../processes/customer-support/flag-an-account-signal.md)

## What to record

Each case leaves its one owner at each point with the date it moved and
why, its state and its clock from the customer's first request, the
records gathered with where each was read, each identity check asked for
with the level it needed, the result and when the pass lapsed, each
promise with who made it, its date and whether it was kept or handed on,
each reminder sent before a date and each promise that passed, each
process it was handed to with the customer's own words and the reference
there, each reply's approver and the version sent where a named person
approved it, what each customer was told and by whom, and its close, any
reopening and the survey started. Each billing question leaves how it
was sorted, the claim or the request sent on, and the date Finance
promised with each time it was raised. Each linked bug or incident
leaves every case linked to it with its next update, and each case
closed or kept open with its reason after an outage. Each account signal
leaves the customer's own words, the kind it was sorted as and who
confirmed it, any risk or opening Sales already held, the reference in
Sales and the date, and what Sales decided with any fix a save plan
names for support. Nothing in the record shows this agent sending a
reply, deciding an answer, deciding a refund, a credit or a dispute,
making an offer or discussing a price, or scoring a support specialist.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
