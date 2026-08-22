---
name: check-what-the-terms-allow
description: Reads the terms attached to a data source, a site or a market and says what may actually be used, targeted, scored on, offered or published. Use it when running `ref/mkt/customer-reviews` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Check what the terms allow

## What it does

Reads the terms attached to a data source, a site or a market and says
what may actually be used, targeted, scored on, offered or published.
Every answer names the term or the rule it rests on, so an agent
planning around it knows where the line is.

## Where it happens

The agent does this in eight activities across seven reference
processes. Each one names the activity as that process words it.

- **Check the Ask against the Rules**
  - `ref/mkt/customer-reviews`, activity 7 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Clear the Data and the Targeting**
  - `ref/mkt/ideal-customer-profile`, activity 11 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Clear the Data and the Traits**
  - `ref/mkt/segment-the-market`, activity 11 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Clear the New Signals**
  - `ref/mkt/lead-scoring-model`, activity 6 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Clear the Sources**
  - `ref/mkt/size-market-opportunity`, activity 11 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Clear the Targeting and the Data**
  - `ref/mkt/media-plan`, activity 4 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Read the Disclosure Rules**
  - `ref/mkt/influencer-campaign`, activity 3 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)
- **Read the Site Rules**
  - `ref/mkt/customer-reviews`, activity 2 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
