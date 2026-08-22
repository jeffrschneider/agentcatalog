---
name: check-claims-against-their-sources
description: Takes a claim somebody wants to publish, finds the source under it, and says whether that source actually carries the claim. Use it when running `ref/mkt/announce-company-news` and 9 other reference processes.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Check claims against their sources

## What it does

Takes a claim somebody wants to publish, finds the source under it, and
says whether that source actually carries the claim. It redoes the
arithmetic behind a figure, reads a number straight out of the system
that holds it, and records the source beside every claim so that the
next person can check the same thing.

## Where it happens

The agent does this in nine activities across ten reference processes.
Each one names the activity as that process words it.

- **Check Whether the Facts Still Hold**
  - `ref/mkt/refresh-content`, activity 6 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Check the Facts**
  - `ref/mkt/customer-case-study`, activity 12 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/long-form-content`, activity 8 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Check the Method**
  - `ref/mkt/size-market-opportunity`, activity 10 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Confirm the Facts**
  - `ref/mkt/announce-company-news`, activity 3 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
  - `ref/mkt/crisis-communication`, activity 2 -
    [Manage Crisis Communication](../../../../processes/marketing/crisis-communication.md)
- **Put a Source Under Every Message**
  - `ref/mkt/brand-voice`, activity 8 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
- **Record the Proof Behind Each Claim**
  - `ref/mkt/product-positioning`, activity 13 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Record the Proof Behind the Promise**
  - `ref/mkt/brand-positioning`, activity 11 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
- **Test the Positions against the Evidence**
  - `ref/mkt/brand-positioning`, activity 7 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
  - `ref/mkt/product-positioning`, activity 9 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Verify the Customer's Results**
  - `ref/mkt/customer-case-study`, activity 7 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/customer-reference`, activity 5 -
    [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
