---
name: take-in-a-claim-and-promise-a-date
description: Takes a claim that a statement or a customer invoice is wrong, acknowledges it, and names who holds it and the date the answer comes, before anybody knows whether the claim is right. Use it when running `ref/fin/resolve-a-billing-dispute`, `ref/rev/settle-a-commission-dispute` and `ref/sup/answer-a-billing-question`.
license: CC-BY-4.0
metadata:
  agent: dispute-coordinator
  agent-version: "1"
---

# Take in a claim and promise a date

## What it does

Takes a claim that a statement or a customer invoice is wrong,
acknowledges it, and names who holds it and the date the answer comes,
before anybody knows whether the claim is right. Puts the claim in a
class, arithmetic, credit, plan wording or bad data, or for an invoice a
price, a quantity or usage, the tax, the terms or work not received,
because the class decides who is heard and what evidence is pulled.

## Where it happens

The agent does this in six activities across three reference processes.
Each one names the activity as that process words it.

- **Acknowledge and Promise a Date**
  - `ref/fin/resolve-a-billing-dispute`, activity 2 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
  - `ref/rev/settle-a-commission-dispute`, activity 2 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Classify the Claim**
  - `ref/fin/resolve-a-billing-dispute`, activity 3 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
  - `ref/rev/settle-a-commission-dispute`, activity 3 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Take In the Claim**
  - `ref/fin/resolve-a-billing-dispute`, activity 1 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
- **Take In the Claim at Finance**
  - `ref/sup/answer-a-billing-question`, activity 10 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)
- **Take in the Claim**
  - `ref/rev/settle-a-commission-dispute`, activity 1 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Tell the Customer Who Holds It Now**
  - `ref/sup/answer-a-billing-question`, activity 11 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)

## What to record

Per claim: the statement, the line, the amount claimed and what the
claimant relies on in their own words; the promised answer date and who
holds the claim; and the class it was put in with the evidence that
class required. The statement frozen at its version with the run version
behind it. Both computations set side by side with every input where
they differ. The plan sentence that governs the line, quoted, at the
version that applies. What the claimant holds that the record does not,
and the other seller's account with what each can show for it. Then the
decision, upheld, partly upheld or refused, with the sentence and the
record behind it; the signature on anything that moves money and the
date the money moves; the answer as sent with its evidence and the
escalation route; the correction the next run is committed to; and
whether the plan, the data or the calculator produced the error. A
refused claim is recorded with its evidence, because the next claim on
the same sentence is the one that changes the plan.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
