---
name: read-where-pages-rank
description: Reads where the organization's pages currently stand in search results, which terms they have lost and what ranks instead, and reports how each published piece did against where it stood before. Use it when running `ref/mkt/marketing-performance-report` and `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Read where pages rank

## What it does

Reads where the organization's pages currently stand in search results,
which terms they have lost and what ranks instead, and reports how each
published piece did against where it stood before.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Account for the Published Pieces**
  - `ref/mkt/marketing-performance-report`, activity 6 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Read Where the Pages Stand in Search**
  - `ref/mkt/refresh-content`, activity 4 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Watch What the Changes Did**
  - `ref/mkt/refresh-content`, activity 20 -
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
