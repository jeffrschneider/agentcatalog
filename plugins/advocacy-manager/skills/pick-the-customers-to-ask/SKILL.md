---
name: pick-the-customers-to-ask
description: Pulls the accounts that match the profile, orders them by how well they fit and how ready they are, and settles who actually gets asked this cycle. Use it when running `ref/mkt/advisory-board` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: advocacy-manager
  agent-version: "1"
---

# Pick the customers to ask

## What it does

Pulls the accounts that match the profile, orders them by how well they
fit and how ready they are, and settles who actually gets asked this
cycle.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Choose the Customers to Ask**
  - `ref/mkt/customer-reviews`, activity 4 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Draw up the Candidate List**
  - `ref/mkt/customer-reference`, activity 3 -
    [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)
- **Rank the Shortlist**
  - `ref/mkt/customer-reference`, activity 6 -
    [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)
- **Settle the Membership**
  - `ref/mkt/advisory-board`, activity 3 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)
- **Take in the Candidate**
  - `ref/mkt/customer-case-study`, activity 1 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)

## What to record

For each ask, it records the customer, what was asked for, who asked,
the date, and the answer that came back. An agreement records its terms
in the customer's own words: what may be used, in which channels, under
which name and title, and until when, together with the approval the use
rests on. A refusal records the reason the customer gave and the date
they may be asked again. Beside those, it keeps a standing list of which
customers are available for which kind of ask, current as of a date, so
that no run plans around a customer who never agreed to it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
