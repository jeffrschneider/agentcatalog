---
name: name-the-opportunities-worth-selling
description: Lists what could be sold into the account, puts a size band on each one, and tests each against the read. Use it when running `ref/sls/write-an-account-plan`.
license: CC-BY-4.0
metadata:
  agent: account-planner
  agent-version: "1"
---

# Name the opportunities worth selling

## What it does

Lists what could be sold into the account, puts a size band on each one,
and tests each against the read. Every opportunity names the buyer
behind it or is marked as having none, and what survives is put in the
order the team goes after it.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **List What Could Be Sold**
  - `ref/sls/write-an-account-plan`, activity 4 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Name Who Buys Each One**
  - `ref/sls/write-an-account-plan`, activity 7 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Put the Opportunities in Order**
  - `ref/sls/write-an-account-plan`, activity 8 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Size Each Opportunity**
  - `ref/sls/write-an-account-plan`, activity 5 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Test Each Opportunity Against the Read**
  - `ref/sls/write-an-account-plan`, activity 6 -
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
