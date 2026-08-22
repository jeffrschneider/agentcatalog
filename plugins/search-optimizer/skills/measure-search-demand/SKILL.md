---
name: measure-search-demand
description: Finds out what people actually search for on a subject and comes back with the terms and the questions, the demand figure behind each one, and the date that figure was pulled. Use it when running `ref/mkt/annual-marketing-plan` and 8 other reference processes.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Measure search demand

## What it does

Finds out what people actually search for on a subject and comes back
with the terms and the questions, the demand figure behind each one, and
the date that figure was pulled. It also reports the words buyers
themselves use for the problem and for the category.

## Where it happens

The agent does this in six activities across nine reference processes.
Each one names the activity as that process words it.

- **Gather How the Audience Talks**
  - `ref/mkt/brand-voice`, activity 3 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
- **Gather the Evidence**
  - `ref/mkt/brand-positioning`, activity 2 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
- **Gather the Market Evidence**
  - `ref/mkt/product-positioning`, activity 3 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Gather the Outside Evidence**
  - `ref/mkt/annual-marketing-plan`, activity 4 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/segment-the-market`, activity 4 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
  - `ref/mkt/size-market-opportunity`, activity 4 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Read the Search Demand**
  - `ref/mkt/content-calendar`, activity 5 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
  - `ref/mkt/map-buyer-journey`, activity 3 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Research the Search Demand**
  - `ref/mkt/paid-search-campaign`, activity 2 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)

## What to record

The search requirement at a version, with every term carrying the demand
figure behind it and the date that figure was pulled. The pre-publish
check as a scored list, with a verdict on each item and the rule behind
every failure. Every recommendation names the element to change and what
it should say, so the agent that owns the page can act on it without a
conversation.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
