---
name: audience-treatment
description: Divides the audience into groups and says how much each group gets, from the money and attention a tier of accounts is worth down to who gets a message, who gets a call and who is left alone, and names who is kept out and which groups must not overlap. Use it when running `ref/mkt/account-based-play`, `ref/mkt/target-audience-segment` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Audience treatment

## What it does

Divides the audience into groups and says how much each group gets, from
the money and attention a tier of accounts is worth down to who gets a
message, who gets a call and who is left alone, and names who is kept
out and which groups must not overlap.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Name the Exclusions**
  - `ref/mkt/target-audience-segment`, activity 5 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Set the Tiers and the Weight**
  - `ref/mkt/account-based-play`, activity 3 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Sort the Segment into Treatments**
  - `ref/mkt/win-back-campaign`, activity 5 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
