---
name: record-the-answer-and-pass-the-deal-on
description: Records what the customer said in their own words, with the date and who heard it, hands the deal to the people who run discovery, and tells the agent that raised the signal what the approach actually produced. Use it when running `ref/sls/open-an-expansion-deal`.
license: CC-BY-4.0
metadata:
  agent: upsell-planner
  agent-version: "1"
---

# Record the answer and pass the deal on

## What it does

Records what the customer said in their own words, with the date and who
heard it, hands the deal to the people who run discovery, and tells the
agent that raised the signal what the approach actually produced.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Hand It to Discovery**
  - `ref/sls/open-an-expansion-deal`, activity 15 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Hear the Answer and Record It**
  - `ref/sls/open-an-expansion-deal`, activity 13 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Tell the Spotter What Happened**
  - `ref/sls/open-an-expansion-deal`, activity 16 -
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
