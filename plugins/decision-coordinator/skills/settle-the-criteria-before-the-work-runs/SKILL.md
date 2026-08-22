---
name: settle-the-criteria-before-the-work-runs
description: Fixes the rules the work will be held to before any candidate arrives, so that nothing is scored against a standard invented after the fact. Use it when running `ref/mkt/engage-marketing-agency` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Settle the criteria before the work runs

## What it does

Fixes the rules the work will be held to before any candidate arrives,
so that nothing is scored against a standard invented after the fact.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Choose the Dividing Traits**
  - `ref/mkt/segment-the-market`, activity 6 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Choose the Sizing Method**
  - `ref/mkt/size-market-opportunity`, activity 3 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Name the Qualifying Signals**
  - `ref/mkt/ideal-customer-profile`, activity 7 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Set the Naming Criteria**
  - `ref/mkt/name-product`, activity 2 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Set the Selection Criteria**
  - `ref/mkt/engage-marketing-agency`, activity 6 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)

## What to record

The decision written down as a question before any evidence is gathered:
what it has to settle, who decides it, what evidence it needs and from
which agent, and the date it is due. The evidence as it came in, each
line attributed to the agent and the source behind it. The candidate
answers, each written out with what it would cost and what it would rule
out. The answer at a version, naming who decided it, on what date, for
what reasons, and anyone who disagreed with what that person said. A
handover line for each agent that has to act on the answer, naming the
agent and what it was given. The review date, set at the moment the
answer is recorded.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
