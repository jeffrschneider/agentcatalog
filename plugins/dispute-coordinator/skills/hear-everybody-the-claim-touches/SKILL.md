---
name: hear-everybody-the-claim-touches
description: Hears the claimant say what they believe happened in their own words, and hears the other seller and its manager whenever credit would move away from somebody. Use it when running `ref/rev/settle-a-commission-dispute`.
license: CC-BY-4.0
metadata:
  agent: dispute-coordinator
  agent-version: "1"
---

# Hear everybody the claim touches

## What it does

Hears the claimant say what they believe happened in their own words,
and hears the other seller and its manager whenever credit would move
away from somebody. Nobody's statement is shown to anybody else.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hear the Claimant**
  - `ref/rev/settle-a-commission-dispute`, activity 8 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Hear the Other Seller**
  - `ref/rev/settle-a-commission-dispute`, activity 9 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)

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
