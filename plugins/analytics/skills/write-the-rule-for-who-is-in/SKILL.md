---
name: write-the-rule-for-who-is-in
description: The agent writes the condition a record has to meet to be in a segment, a program or a pool, how long it stays in, and which treatment it gets. Use it when running `ref/mkt/display-retargeting` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Write the rule for who is in

## What it does

The agent writes the condition a record has to meet to be in a segment,
a program or a pool, how long it stays in, and which treatment it gets.
The rule is written so somebody else can build the list from it and get
the same answer.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Define Who Enters**
  - `ref/mkt/nurture-sequence`, activity 2 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Define the Retargeting Pools**
  - `ref/mkt/display-retargeting`, activity 4 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Sort the Segment into Treatments**
  - `ref/mkt/win-back-campaign`, activity 5 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Write the Membership Rule**
  - `ref/mkt/target-audience-segment`, activity 4 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
