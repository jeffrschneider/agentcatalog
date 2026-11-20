---
name: record-a-write-off
description: Records each approved write-off for exactly the amount approved against the allowance, passes the tax and the period's write-offs on, and keeps the account open so that a later payment is applied as a recovery. Use it when running `ref/fin/write-off-a-bad-debt`.
license: CC-BY-4.0
metadata:
  agent: receivables-keeper
  agent-version: "1"
---

# Record a write off

## What it does

Records each approved write-off for exactly the amount approved against
the allowance, passes the tax and the period's write-offs on, and keeps
the account open so that a later payment is applied as a recovery.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Keep the Account Open for Recovery**
  - `ref/fin/write-off-a-bad-debt`, activity 15 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)
- **Pass the Write-Off to Tax and the Close**
  - `ref/fin/write-off-a-bad-debt`, activity 11 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)
- **Record the Write-Off with Its Approval**
  - `ref/fin/write-off-a-bad-debt`, activity 10 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)

## What to record

Each day leaves every receipt on the bank's report with the remittance
kept beside it, the customer identified or the reason it could not be,
each match with the rule that made it, each receipt applied or held with
its reason, and the applied and held amounts agreed to the bank's total.
Each held receipt leaves the customer's answer, the named person's
decision and what was applied, kept on account or passed for refund, and
each customer's account shows every open invoice, its age and anything
held or in dispute. Each overdue invoice leaves the check that it was
still owed, each promise set against the receipts on its date, and the
outcome. Each write-off leaves the amount still owed on each invoice,
the security and other routes, the proposal as set out, the write-off
recorded for exactly the amount approved with the approval and its
version attached, the notice to tax and to the close, and any later
payment applied as a recovery. Nothing in the record shows this agent
clearing a shortfall, moving money between customers, refunding money or
writing off a debt on its own.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
