---
name: check-a-name-in-search
description: Reads what a candidate name already collides with in search results and what the rest of the category is called, so the organization knows what the name would be competing against. Use it when running `ref/mkt/name-product`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Check a name in search

## What it does

Reads what a candidate name already collides with in search results and
what the rest of the category is called, so the organization knows what
the name would be competing against.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Name in Search**
  - `ref/mkt/name-product`, activity 10 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Read the Naming Landscape**
  - `ref/mkt/name-product`, activity 3 -
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
