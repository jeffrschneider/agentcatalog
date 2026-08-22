---
name: restate-the-price-everywhere-it-is-published
description: Every live page, ad and asset that names a price. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Restate the Price Everywhere It Is Published

## What happens

Every live page, ad and asset that names a price.

## Where it happens

- `ref/mkt/pricing-change`, activity 7 -
  [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
