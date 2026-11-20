---
name: forecast-cash
description: Opens each week's forecast from the last version, adds the paydays, the tax and the debt service, builds cash by week and then by month for each entity and currency, explains every change from last week, sets last week's forecast beside what happened, tests each week against the minimum and the room in each facility, sets out the options for a shortfall, and publishes the forecast once it is reviewed. Use it when running `ref/fin/forecast-cash`.
license: CC-BY-4.0
metadata:
  agent: treasury-analyst
  agent-version: "1"
---

# Forecast cash

## What it does

Opens each week's forecast from the last version, adds the paydays, the
tax and the debt service, builds cash by week and then by month for each
entity and currency, explains every change from last week, sets last
week's forecast beside what happened, tests each week against the
minimum and the room in each facility, sets out the options for a
shortfall, and publishes the forecast once it is reviewed.

## Where it happens

The agent does this in nine activities across one reference process.
Each one names the activity as that process words it.

- **Add Payroll, Tax and Debt**
  - `ref/fin/forecast-cash`, activity 4 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Build the Forecast**
  - `ref/fin/forecast-cash`, activity 6 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Compare Last Week with What Happened**
  - `ref/fin/forecast-cash`, activity 8 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Explain the Change from Last Week**
  - `ref/fin/forecast-cash`, activity 7 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Open the Week's Forecast**
  - `ref/fin/forecast-cash`, activity 1 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Publish the Forecast**
  - `ref/fin/forecast-cash`, activity 13 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Record What the Forecast Taught**
  - `ref/fin/forecast-cash`, activity 14 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Set Out the Options for a Shortfall**
  - `ref/fin/forecast-cash`, activity 10 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)
- **Test Against the Minimum and the Facilities**
  - `ref/fin/forecast-cash`, activity 9 -
    [Forecast Cash](../../../../processes/finance/forecast-cash.md)

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
