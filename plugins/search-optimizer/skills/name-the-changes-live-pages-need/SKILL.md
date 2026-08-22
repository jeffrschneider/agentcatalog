---
name: name-the-changes-live-pages-need
description: Sweeps the pages that are already live to find every one carrying something that has changed, and names the element on each page and what it should now say. Use it when running `ref/mkt/feature-release` and `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Name the changes live pages need

## What it does

Sweeps the pages that are already live to find every one carrying
something that has changed, and names the element on each page and what
it should now say.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Restate the Price Everywhere It Is Published**
  - `ref/mkt/pricing-change`, activity 7 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Update the Product Pages**
  - `ref/mkt/feature-release`, activity 6 -
    [Announce Feature Release](../../../../processes/marketing/feature-release.md)

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
