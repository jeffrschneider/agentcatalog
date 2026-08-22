---
name: change-a-published-price
description: Finds every live page, ad and asset that names a price and changes it, puts the new pages up, and points the old addresses at them. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Change a published price

## What it does

Finds every live page, ad and asset that names a price and changes it,
puts the new pages up, and points the old addresses at them.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Change the Public Price**
  - `ref/mkt/pricing-change`, activity 12 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Restate the Price Everywhere It Is Published**
  - `ref/mkt/pricing-change`, activity 7 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
