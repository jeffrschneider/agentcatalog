---
name: research-sampling
description: Draws the people a study will ask, in a way that represents the market the study is meant to speak for, including drawing two groups that match each other when the study compares them. Use it when running `ref/mkt/brand-health`, `ref/mkt/customer-research` and `ref/mkt/win-loss-analysis`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Research sampling

## What it does

Draws the people a study will ask, in a way that represents the market
the study is meant to speak for, including drawing two groups that match
each other when the study compares them.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Define the Sample**
  - `ref/mkt/brand-health`, activity 7 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 6 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Draw Both Samples**
  - `ref/mkt/win-loss-analysis`, activity 5 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)

## What to record

Each program at a version, naming the entry condition, every step, every
wait, the condition on every branch, and every exit. The hygiene cycle's
scope at a version, saying which records it covers and what it has to
fix in them. The rule that settles which program takes a contact who
qualifies for two, with the date it was decided and who decided it. A
dated account of the database between cycles: how many records there
are, how many are complete enough to use, and how many may be contacted.
The CONVENED and DONE records of everything it convenes. The go record
for a program, naming the version that started sending and who said go.
The standing readout at the cadence the process sets, and the decision
it made after reading it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
