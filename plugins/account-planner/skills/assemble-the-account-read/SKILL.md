---
name: assemble-the-account-read
description: "Reads an account into one document: what it wants, what is going on inside it, and what nothing answered. Use it when running `ref/sls/research-an-account`."
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Assemble the account read

## What it does

Reads an account into one document: what it wants, what is going on
inside it, and what nothing answered. Every line names where it came
from and the date that value was current, and the read is issued at a
version with a date to take it again.

## Where it happens

The agent does this in eight activities across one reference process.
Each one names the activity as that process words it.

- **Assemble the Account Read**
  - `ref/sls/research-an-account`, activity 12 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Issue the Read at a Version**
  - `ref/sls/research-an-account`, activity 14 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Mark What Is Unknown**
  - `ref/sls/research-an-account`, activity 11 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Review the Read with the Owner**
  - `ref/sls/research-an-account`, activity 13 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Set the Refresh Date**
  - `ref/sls/research-an-account`, activity 15 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Set the Research Questions**
  - `ref/sls/research-an-account`, activity 2 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Take in the Account**
  - `ref/sls/research-an-account`, activity 1 -
    [Research an Account](../../../../processes/sales/research-an-account.md)
- **Work out What the Account Wants**
  - `ref/sls/research-an-account`, activity 6 -
    [Research an Account](../../../../processes/sales/research-an-account.md)

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
