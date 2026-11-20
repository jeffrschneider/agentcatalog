---
name: propose-a-limit
description: Proposes a limit, payment terms and any security the policy asks for, with the evidence behind each figure beside it, and records the account owner's view beside the proposal. Use it when running `ref/fin/set-a-customers-credit-limit`.
license: CC-BY-4.0
metadata:
  agent: credit-analyst
  agent-version: "1"
---

# Propose a limit

## What it does

Proposes a limit, payment terms and any security the policy asks for,
with the evidence behind each figure beside it, and records the account
owner's view beside the proposal.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hear the Account Owner**
  - `ref/fin/set-a-customers-credit-limit`, activity 7 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Propose a Limit and Terms**
  - `ref/fin/set-a-customers-credit-limit`, activity 6 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)

## What to record

Each credit run leaves what opened it, the legal entity that will be
billed with any parent or guarantor, the payment history with its dates,
the reports and filings with their sources and the dates they were read,
the rating with the policy rule and version behind each part, and any
part the evidence cannot support named as unsupported. Beside them sit
the proposed limit, terms and security with the evidence behind each
figure, the account owner's view, the approver's decision as recorded,
the review date with the warning signs to watch, and the follow-up level
passed to collections. Each review during collection leaves what opened
it and what it found. Nothing in the record shows this agent setting,
recording or changing a limit, or holding an order.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
