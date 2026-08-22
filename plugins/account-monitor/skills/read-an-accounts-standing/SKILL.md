---
name: read-an-accounts-standing
description: The agent reads one named account across the systems that hold it, covering product usage, support history, contract terms and where the account sits in the renewal cycle. Use it when running `ref/mkt/account-based-play` and 7 other reference processes.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Read an accounts standing

## What it does

The agent reads one named account across the systems that hold it,
covering product usage, support history, contract terms and where the
account sits in the renewal cycle. Every answer comes back with what
each system said and when that reading was current.

## Where it happens

The agent does this in seven activities across eight reference
processes. Each one names the activity as that process words it.

- **Check Each Account's Standing**
  - `ref/mkt/customer-reference`, activity 4 -
    [Recruit Customer Reference](../../../../processes/marketing/customer-reference.md)
- **Check What the Partner Holds**
  - `ref/mkt/enable-channel-partner`, activity 2 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Check Where the Account Stands**
  - `ref/mkt/customer-case-study`, activity 2 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/customer-newsletter`, activity 3 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- **Confirm the Signal**
  - `ref/mkt/churn-risk-play`, activity 2 -
    [Run Churn-Risk Play](../../../../processes/marketing/churn-risk-play.md)
- **Read the Account**
  - `ref/mkt/onboarding-email-program`, activity 2 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Read the Accounts**
  - `ref/mkt/account-based-play`, activity 2 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Read the Product's Own Record**
  - `ref/mkt/product-positioning`, activity 4 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)

## What to record

For each question it answers, it records the account, what was asked,
the answer, the date, and every system it read with the value it found
and when that value was current. A milestone answer names the milestone
list at its version and says which of those milestones the account has
met. A risk signal is recorded whichever way it was judged, with the
reading that settled it. Anything it could not read is recorded as
unread instead of being left out of the answer.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
