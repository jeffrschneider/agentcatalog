---
name: read-the-sentence-behind-a-contested-line
description: Reads out the plan sentence that governs a disputed line, at the version the claimant signed rather than the current one. Use it when running `ref/rev/calculate-commission` and `ref/rev/settle-a-commission-dispute`.
license: CC-BY-4.0
metadata:
  agent: plan-designer
  agent-version: "1"
---

# Read the sentence behind a contested line

## What it does

Reads out the plan sentence that governs a disputed line, at the version
the claimant signed rather than the current one. Takes back the
corrections a run had to make and the cause behind a settled claim, and
carries an ambiguous sentence into the next period's design.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Feed the Cause Back**
  - `ref/rev/settle-a-commission-dispute`, activity 15 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Read the Plan Sentence That Governs It**
  - `ref/rev/settle-a-commission-dispute`, activity 7 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Record the Corrections**
  - `ref/rev/calculate-commission`, activity 16 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)

## What to record

Per period: the intent as leadership wrote it, what last period's plans
paid seller by seller next to what those sellers did, and the outcomes
each role is paid to reach at a version leadership holds. The sellers,
their quotas and the money available. The draft shape per role with
every rate, gate, cap and accelerator written down and tied to a named
outcome. The cost at each attainment outcome, seller by seller and in
total, with the assumptions it rests on. Every awkward case, what the
draft pays for it, and whether that was meant. Every pay rule the draft
touches and what it would take to stand on it. The cost as finance
accepted it, the signed shape at a version, the wording as published,
the worked examples computed the way the calculator will compute the
real thing, who received which plan on what date at which version, who
signed and who did not and what the unsigned objected to, and what the
plan does not answer yet.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
