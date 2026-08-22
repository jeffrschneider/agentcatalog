---
name: watch-a-first-deal-and-close-the-run-out
description: Watches a first deal while the partner leads it and says when it is slipping, so a person can decide whether a stage is taken back. Use it when running `ref/prt/onboard-a-partner` and `ref/prt/run-a-first-deal-together`.
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Watch a first deal and close the run out

## What it does

Watches a first deal while the partner leads it and says when it is
slipping, so a person can decide whether a stage is taken back. Then it
debriefs what the partner did alone and what the company did for them,
hands the relationship to its ongoing manager, and records where a setup
run stalled for the next one.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Debrief with the Partner**
  - `ref/prt/run-a-first-deal-together`, activity 14 -
    [Run a First Deal Together](../../../../processes/partners/run-a-first-deal-together.md)
- **Hand the Partner to Their Ongoing Manager**
  - `ref/prt/run-a-first-deal-together`, activity 16 -
    [Run a First Deal Together](../../../../processes/partners/run-a-first-deal-together.md)
- **Record What the Onboarding Cost**
  - `ref/prt/onboard-a-partner`, activity 16 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)
- **Step In When It Slips**
  - `ref/prt/run-a-first-deal-together`, activity 12 -
    [Run a First Deal Together](../../../../processes/partners/run-a-first-deal-together.md)

## What to record

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
