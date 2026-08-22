---
name: set-the-profile-and-the-rules
description: Writes down which customer would fit the ask, what the ask may offer, and what it has to disclose. Use it when running `ref/mkt/customer-reference` and `ref/mkt/customer-reviews`.
license: CC-BY-4.0
metadata:
  agent: advocacy-manager
  agent-version: "1"
---

# Set the profile and the rules

## What it does

Writes down which customer would fit the ask, what the ask may offer,
and what it has to disclose. It reads each site's own policy on asking
and on incentives first, because those policies differ and some forbid
an incentive outright.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Read the Site Rules**
  - `ref/mkt/customer-reviews`, activity 2 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Set the Reference Profile**
  - `ref/mkt/customer-reference`, activity 2 -
    [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)
- **Set the Rules for Asking**
  - `ref/mkt/customer-reviews`, activity 3 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)

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
