---
name: set-the-timing-and-the-range
description: Sets the window the ask lands in against the renewal date, the notice period and the budget cycle, and puts a range on it inside the discount authority that already exists. Use it when running `ref/sls/open-an-expansion-deal`.
license: CC-BY-4.0
metadata:
  agent: upsell-planner
  agent-version: "1"
---

# Set the timing and the range

## What it does

Sets the window the ask lands in against the renewal date, the notice
period and the budget cycle, and puts a range on it inside the discount
authority that already exists. Every contract date that constrains the
window is named.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Put a Range on It**
  - `ref/sls/open-an-expansion-deal`, activity 7 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Set the Timing Against the Contract**
  - `ref/sls/open-an-expansion-deal`, activity 6 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)

## What to record

Per run: the approach at a version, saying what would be proposed, to
whom, in what order, and what the customer gets out of it. What adopting
it costs the customer in work, training and disruption, said plainly.
The window the ask lands in, with every contract date that constrains
it. The range with its assumptions and the authority it sits inside. The
approach as the relationship owner agreed it, with anything they struck
out kept rather than dropped. Who says what to whom and when. What
delivery said, and what carrying it would take from them. The signed
ask, the range and the timing, and the signer. The approach as it was
actually made, to whom, on what date. What the customer said in their
own words, with the date and who said it. The deal as handed to
discovery, and the outcome set against what the signal predicted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
