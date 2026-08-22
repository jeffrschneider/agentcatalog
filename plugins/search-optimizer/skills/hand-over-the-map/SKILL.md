---
name: hand-over-the-map
description: Each receiving agent says what it changes. Use it when running `ref/mkt/map-buyer-journey`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Hand over the Map

## What happens

Each receiving agent says what it changes.

## Where it happens

- `ref/mkt/map-buyer-journey`, activity 17 -
  [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)

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
