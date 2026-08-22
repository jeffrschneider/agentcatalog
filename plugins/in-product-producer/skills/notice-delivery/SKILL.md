---
name: notice-delivery
description: Works out which accounts should see the notice out of the accounts that actually have the feature, switches it on, and keeps the record of who was told and when. Use it when running `ref/mkt/feature-release` and `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: in-product-producer
  agent-version: "1"
---

# Notice delivery

## What it does

Works out which accounts should see the notice out of the accounts that
actually have the feature, switches it on, and keeps the record of who
was told and when. The same work covers a notice a customer is owed and
a notice that simply announces something new.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Serve the Notice**
  - `ref/mkt/pricing-change`, activity 10 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Tell the Customers Who Have It**
  - `ref/mkt/feature-release`, activity 7 -
    [Announce Feature Release](../../../../processes/marketing/feature-release.md)

## What to record

The notice at a version, with a preview that shows it the way an account
will see it. The audience at a version, with the count of accounts that
have the feature, the count left after the exclusion rules were applied,
and the rule behind every removal. The run settings as they were set,
naming where in the product the notice appears, the date it starts, the
date it ends, and how often one person sees it. The go record naming the
version that went live, the time it was switched on, and the person who
said go. The takedown record naming the version that came down and the
date it came down. The report afterwards, giving the accounts that saw
the notice, the people who did what it asked, the people who dismissed
it and the people who did nothing. Anything it could not verify is
recorded as unverified instead of being left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
