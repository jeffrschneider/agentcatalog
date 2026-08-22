---
name: check-a-page-before-it-goes-live
description: Reads a finished or changed page and scores the things that decide whether it can be found and used, which are the title, the headings, the internal links, the address, the load time, the accessibility and the tracking. Use it when running `ref/mkt/brand-refresh` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: search-optimizer
  agent-version: "1"
---

# Check a page before it goes live

## What it does

Reads a finished or changed page and scores the things that decide
whether it can be found and used, which are the title, the headings, the
internal links, the address, the load time, the accessibility and the
tracking. Each failure names the element to change and what it should
say.

## Where it happens

The agent does this in five activities across six reference processes.
Each one names the activity as that process words it.

- **Check the Changed Page**
  - `ref/mkt/website-content-update`, activity 10 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Check the Changed Pages**
  - `ref/mkt/refresh-content`, activity 18 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Check the Finished Page**
  - `ref/mkt/customer-case-study`, activity 17 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/long-form-content`, activity 13 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Check the Remade Material**
  - `ref/mkt/brand-refresh`, activity 17 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Score the Page**
  - `ref/mkt/landing-page`, activity 9 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)

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
