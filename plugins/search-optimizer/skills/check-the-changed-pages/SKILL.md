---
name: check-the-changed-pages
description: Accessibility, links, load, headings and tracking. Use it when running `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Check the Changed Pages

## What happens

Accessibility, links, load, headings and tracking.

## Where it happens

- `ref/mkt/refresh-content`, activity 18 -
  [Refresh Published Content](../../../../processes/marketing/refresh-content.md)

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
