---
name: set-the-search-requirement
description: Turns the demand into a short list of terms and questions a page or a piece has to cover if anyone is going to find it, and delivers that list before the writing starts. Use it when running `ref/mkt/landing-page`, `ref/mkt/long-form-content` and `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Set the search requirement

## What it does

Turns the demand into a short list of terms and questions a page or a
piece has to cover if anyone is going to find it, and delivers that list
before the writing starts.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Name the Search Terms**
  - `ref/mkt/landing-page`, activity 3 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Set What Each Page Has to Answer**
  - `ref/mkt/refresh-content`, activity 11 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Set the Search Terms**
  - `ref/mkt/long-form-content`, activity 2 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)

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
