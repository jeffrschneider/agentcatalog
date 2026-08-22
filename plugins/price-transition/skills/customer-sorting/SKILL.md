---
name: customer-sorting
description: Goes through the customers a change affects one at a time, works out what each pays now and what the new prices make them pay, and applies the rules to say which group the customer falls in and which notice they are owed. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: price-transition
  agent-version: "1"
---

# Customer sorting

## What it does

Goes through the customers a change affects one at a time, works out
what each pays now and what the new prices make them pay, and applies
the rules to say which group the customer falls in and which notice they
are owed. The result is one register and one list per treatment.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Build the Notice Lists**
  - `ref/mkt/pricing-change`, activity 9 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Read the Affected Customers**
  - `ref/mkt/pricing-change`, activity 2 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

The register at a version, giving for each customer what they pay now,
what the new prices make them pay, the amount and the share of the
change, the grandfathering rule that caught them and the date that rule
runs out, the notice they are owed, and the earliest date their change
may take effect. A dated line for every notice served, naming the
customer, the version of the wording that went, the date it went, the
route it went by, and the date its waiting time runs out. A dated line
for every price change released, naming the customer, the date the new
price takes effect, and the notice record that cleared it. A customer it
could not sort is recorded as unsorted, with what is missing, rather
than being left out of the register. A change it is holding back is
recorded as held, with the reason and the number of days it has been
held.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
