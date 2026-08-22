---
name: sign-and-issue-the-plan
description: Puts the plan to the people who have to sign it, issues the signed version to everyone who acts on it, and sets the date it comes back up along with the tripwires that bring it back sooner. Use it when running `ref/sls/write-an-account-plan`.
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Sign and issue the plan

## What it does

Puts the plan to the people who have to sign it, issues the signed
version to everyone who acts on it, and sets the date it comes back up
along with the tripwires that bring it back sooner.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Issue the Plan and Tell the Readers**
  - `ref/sls/write-an-account-plan`, activity 15 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Set the Review Date and the Tripwires**
  - `ref/sls/write-an-account-plan`, activity 16 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Sign the Plan**
  - `ref/sls/write-an-account-plan`, activity 14 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)

## What to record

The account read at a version, every line naming the system or document
it came from and the date that value was current, with the questions
nothing answered left standing as unknown. The plan at a version: each
opportunity with the evidence for it and against it, its buyer or the
note that it has none, its size in a confidence band, the order and what
each step depends on the one before it delivering, the assumptions
written as testable statements, the risks and what the plan does about
each, the moves with their owners and dates, and the asks naming who had
to agree. The signed version names both signers and the date. At review,
each plan is scored against what it said when it was signed, and every
decision records who made it, on what evidence, and anyone who
disagreed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
