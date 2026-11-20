---
name: build-the-daily-cash-position
description: Gathers every bank's balances and movements each morning, chases a report that has not arrived, matches each movement to the receipts, payments and transfers that were expected, holds aside anything nobody expected, and builds one position by account, entity and currency that it sets beside the minimum and the forecast and sends to the treasurer. Use it when running `ref/fin/pay-approved-invoices` and `ref/fin/report-the-daily-cash-position`.
license: CC-BY-4.0
metadata:
  agent: treasury-analyst
  agent-version: "1"
---

# Build the daily cash position

## What it does

Gathers every bank's balances and movements each morning, chases a
report that has not arrived, matches each movement to the receipts,
payments and transfers that were expected, holds aside anything nobody
expected, and builds one position by account, entity and currency that
it sets beside the minimum and the forecast and sends to the treasurer.
It also checks each supplier payment run against the cash that must
cover it, and records the released payments in the position.

## Where it happens

The agent does this in thirteen activities across two reference
processes. Each one names the activity as that process words it.

- **Build the Cash Position**
  - `ref/fin/report-the-daily-cash-position`, activity 8 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Chase a Missing Bank Report**
  - `ref/fin/report-the-daily-cash-position`, activity 2 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Check the Cash to Cover the Run**
  - `ref/fin/pay-approved-invoices`, activity 5 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)
- **Compare with the Minimum and the Forecast**
  - `ref/fin/report-the-daily-cash-position`, activity 9 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Gather the Bank Balances**
  - `ref/fin/report-the-daily-cash-position`, activity 1 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Hold Aside Anything Unexpected**
  - `ref/fin/report-the-daily-cash-position`, activity 7 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **List the Payments Due Today**
  - `ref/fin/report-the-daily-cash-position`, activity 5 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Match Each Movement to What Was Expected**
  - `ref/fin/report-the-daily-cash-position`, activity 6 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Read the Bank Movements**
  - `ref/fin/report-the-daily-cash-position`, activity 3 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Record What the Day Taught**
  - `ref/fin/report-the-daily-cash-position`, activity 14 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Record the Day's Position**
  - `ref/fin/report-the-daily-cash-position`, activity 13 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Send the Position to the Treasurer**
  - `ref/fin/report-the-daily-cash-position`, activity 10 -
    [Report the Daily Cash Position](../../../../processes/finance/report-the-daily-cash-position.md)
- **Update the Cash Position**
  - `ref/fin/pay-approved-invoices`, activity 15 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)

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
