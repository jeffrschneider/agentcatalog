---
name: follow-up-with-the-employee
description: Asks the employee for each missing receipt or reason, or about a line that repeats earlier spend, and records what each claim taught. Use it when running `ref/fin/reimburse-an-expense-claim`.
license: CC-BY-4.0
metadata:
  agent: expense-check
  agent-version: "1"
---

# Follow up with the employee

## What it does

Asks the employee for each missing receipt or reason, or about a line
that repeats earlier spend, and records what each claim taught.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Ask the Employee About a Line**
  - `ref/fin/reimburse-an-expense-claim`, activity 5 -
    [Reimburse an Expense Claim](../../../../processes/finance/reimburse-an-expense-claim.md)
- **Record What the Claim Taught**
  - `ref/fin/reimburse-an-expense-claim`, activity 13 -
    [Reimburse an Expense Claim](../../../../processes/finance/reimburse-an-expense-claim.md)

## What to record

Each claim and each card transaction leaves every line with its receipt,
its business reason, its amount and currency, the rate it was converted
at, and the policy rule and version it was read against, returned as
inside the policy, outside it with the rule it breaks, or missing its
evidence. Beside each line sit any earlier claim, card transaction or
booking it repeats, any part marked as treated as pay with the rule
behind it, each question asked of the employee with the answer, and each
reminder sent to the manager. Each claim closes with which lines were
outside the policy and why, which rules caught most and how long the
claim took. Nothing in the record shows this agent approving, refusing
or paying a line.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
