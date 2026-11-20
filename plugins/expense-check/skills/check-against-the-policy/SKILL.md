---
name: check-against-the-policy
description: Takes in each claim, and sets every line and every card transaction against its receipt, its business reason and the limit for its kind, returning each as inside the policy, outside it with the rule it breaks, or missing its evidence. Use it when running `ref/fin/reconcile-company-card-spend` and `ref/fin/reimburse-an-expense-claim`.
license: CC-BY-4.0
metadata:
  agent: expense-check
  agent-version: "1"
---

# Check against the policy

## What it does

Takes in each claim, and sets every line and every card transaction
against its receipt, its business reason and the limit for its kind,
returning each as inside the policy, outside it with the rule it breaks,
or missing its evidence.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check Each Line Against the Policy**
  - `ref/fin/reimburse-an-expense-claim`, activity 2 -
    [Reimburse an Expense Claim](../../../../processes/finance/reimburse-an-expense-claim.md)
- **Check Each Transaction Against the Policy**
  - `ref/fin/reconcile-company-card-spend`, activity 5 -
    [Reconcile Company Card Spend](../../../../processes/finance/reconcile-company-card-spend.md)
- **Take In the Claim**
  - `ref/fin/reimburse-an-expense-claim`, activity 1 -
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
