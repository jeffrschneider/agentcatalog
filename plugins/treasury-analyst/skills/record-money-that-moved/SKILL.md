---
name: record-money-that-moved
description: Matches each placement to the bank's confirmation and each payroll funding to the payments that left, explains what is left in the payroll account, records each transfer and funding with the approval and the release behind it for the ledger, records a transfer between two entities as a balance each owes the other, and records what the run taught. Use it when running `ref/fin/fund-the-payroll` and `ref/fin/move-cash-between-accounts`.
license: CC-BY-4.0
metadata:
  agent: treasury-analyst
  agent-version: "1"
---

# Record money that moved

## What it does

Matches each placement to the bank's confirmation and each payroll
funding to the payments that left, explains what is left in the payroll
account, records each transfer and funding with the approval and the
release behind it for the ledger, records a transfer between two
entities as a balance each owes the other, and records what the run
taught.

## Where it happens

The agent does this in seven activities across two reference processes.
Each one names the activity as that process words it.

- **Explain What Is Left in the Account**
  - `ref/fin/fund-the-payroll`, activity 13 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Match the Funding to the Payments**
  - `ref/fin/fund-the-payroll`, activity 12 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Match the Placement Confirmation**
  - `ref/fin/move-cash-between-accounts`, activity 10 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Record What the Run Taught**
  - `ref/fin/fund-the-payroll`, activity 15 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
  - `ref/fin/move-cash-between-accounts`, activity 13 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Record a Balance Between Entities**
  - `ref/fin/move-cash-between-accounts`, activity 12 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Record the Funding**
  - `ref/fin/fund-the-payroll`, activity 14 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Record the Transfer**
  - `ref/fin/move-cash-between-accounts`, activity 11 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)

## What to record

Each morning leaves every account's balance and movements with the
report they came from, each report chased and each account marked
unreported with its last known balance, each movement matched to what
was expected, each item held aside with its amount, its account and its
reference, and the position by account, entity and currency set beside
the minimum and the forecast, with the time it reached the treasurer and
each exception with the decision on it and the person who made it. Each
week leaves the forecast at its version with every line naming its
source and its assumption, every change from the last version traced to
its cause, last week's forecast beside what happened with the reason for
each miss, the headroom in each week, each shortfall with its options
and the CFO's decision, and the people the forecast went to. Each
transfer and each payroll funding leaves the need or the register behind
it, the amount and how it was worked out, the placements set out, the
transfer as prepared, the approval and the release by people who did not
prepare it, the wire-check agent's confirmation of where it landed, each
placement matched to its confirmation, the entries recorded for the
ledger, and any balance between entities on both ledgers. A funding also
leaves its match to the payments that left the payroll account and the
explanation of what was left there. Each bank change leaves the request
with its confirmation through a contact already on file, the time a
leaver's access ended, the account as it stood, the check of dual
control, the approval, the forms as filled in, the bank's confirmation,
the record as updated and the bank's own list set beside it. Each
covenant test leaves each definition as read, each covenant worked out
with every adjustment and its headroom, the undertakings checked, each
risk raised with the date the CFO heard of it, the certificate as
drafted, signed and sent, and the lenders' acknowledgment. Nothing in
the record shows this agent approving or releasing a payment, choosing
how to meet a shortfall, approving a bank change or signing a
certificate.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
