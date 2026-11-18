---
name: match-incoming-money
description: Sees incoming money cleared in the fund's account and matches each amount to the investor, the call or the sale it belongs to, holding aside anything late, short, over or sent from an account not on record. Use it when running `ref/pc/issue-a-capital-call`, `ref/pc/make-a-distribution` and `ref/pc/run-a-sale-process`.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Match incoming money

## What it does

Sees incoming money cleared in the fund's account and matches each
amount to the investor, the call or the sale it belongs to, holding
aside anything late, short, over or sent from an account not on record.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Confirm the Cash Has Arrived**
  - `ref/pc/make-a-distribution`, activity 2 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Confirm the Money Has Arrived**
  - `ref/pc/run-a-sale-process`, activity 18 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Match Each Receipt**
  - `ref/pc/issue-a-capital-call`, activity 12 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)

## What to record

Each instruction checked leaves the account as it was received, the
channel it came in, the contact called and where that contact's number
came from, the date, the person reached and the result, verified or
held. A change to instructions close to a closing or a pay date is
recorded as suspect until it is verified again, and a change that
arrived by email alone is recorded with the report of it as an attempted
fraud. At a closing, each payment released is recorded against the
verified line of the funds flow it pays, and each payee's receipt is
matched to its line. For a capital call, the fund's receiving account on
each notice is recorded as checked, and each receipt is matched to an
investor, a call and an amount, with anything late, short, over or from
an account not on record held aside with the reason. For a sale and a
distribution, the proceeds are recorded as cleared in the fund's account
with any escrow, holdback or later payment named, and each payment is
matched to its bank confirmation, with anything rejected or returned
held aside. Each call and distribution leaves a reconciliation of what
was called or approved, what was received or paid, and what was booked,
investor by investor, with the bank balance agreed to the books. Nothing
in the record shows this agent releasing a payment, because it holds no
right to.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
