---
name: find-what-is-worth-making
description: Collects what people ask at each stage, finds the questions with nothing published behind them, gathers the topics other agents want made, and scores each candidate against the goals and the evidence. Use it when running `ref/mkt/content-calendar` and `ref/mkt/map-buyer-journey`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Find what is worth making

## What it does

Collects what people ask at each stage, finds the questions with nothing
published behind them, gathers the topics other agents want made, and
scores each candidate against the goals and the evidence.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Collect the Questions**
  - `ref/mkt/map-buyer-journey`, activity 10 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Collect the Topic Candidates**
  - `ref/mkt/content-calendar`, activity 4 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Find the Gaps**
  - `ref/mkt/map-buyer-journey`, activity 13 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Score the Candidates**
  - `ref/mkt/content-calendar`, activity 8 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)

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
