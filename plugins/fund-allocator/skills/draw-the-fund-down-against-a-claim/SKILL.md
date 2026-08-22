---
name: draw-the-fund-down-against-a-claim
description: Scores each claimed cost against the eligible activity list, records the payment and draws the partner's fund down against it, and puts back whatever the claim did not use. Use it when running `ref/prt/check-and-pay-a-claim`.
license: CC-BY-4.0
metadata:
  agent: fund-allocator
  agent-version: "1"
---

# Draw the fund down against a claim

## What it does

Scores each claimed cost against the eligible activity list, records the
payment and draws the partner's fund down against it, and puts back
whatever the claim did not use.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check Each Cost Is Eligible**
  - `ref/prt/check-and-pay-a-claim`, activity 5 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Pay the Partner**
  - `ref/prt/check-and-pay-a-claim`, activity 13 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Release the Money Not Used**
  - `ref/prt/check-and-pay-a-claim`, activity 14 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)

## What to record

The allocation rule at a version, with the date it was published and the
date every partner was told. Per partner, the amount and the exact
inputs the rule read to produce it. The eligible activity list at a
version, saying what is excluded as well as what is included. The
amounts summed against the approved budget, and the difference. Per
request: the eligibility finding naming the list version it was scored
against, the balance at the time, the organization's share with the
match and the cap applied, the decision and the reason it rests on. Per
commitment: the amount held, the partner's fund it came from, and the
date it expires. Per release: what went back to the fund and why. At the
period close, what was allocated, committed, claimed, paid, released and
moved. Any auditor can recompute a partner's allocation from the rule
version and the recorded inputs.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
