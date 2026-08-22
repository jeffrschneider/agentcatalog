---
name: check-the-name-in-search
description: What the name already collides with in results. Use it when running `ref/mkt/name-product`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Check the Name in Search

## What happens

What the name already collides with in results.

## Where it happens

- `ref/mkt/name-product`, activity 10 -
  [Name Product or Company](../../../../processes/marketing/name-product.md)

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
