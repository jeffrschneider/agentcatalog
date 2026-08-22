---
name: watch-an-account-after-contact
description: "Once something has been sent or a change has landed, the agent keeps reading the account and reports what it did: the usage, the replies, the support requests, the deals registered, the milestones reached and where the renewal now stands. Use it when running `ref/mkt/account-based-play` and 4 other reference processes."
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Watch an account after contact

## What it does

Once something has been sent or a change has landed, the agent keeps
reading the account and reports what it did: the usage, the replies, the
support requests, the deals registered, the milestones reached and where
the renewal now stands.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Watch Engagement by Account**
  - `ref/mkt/account-based-play`, activity 16 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Watch What the Account Does**
  - `ref/mkt/churn-risk-play`, activity 10 -
    [Run Churn-Risk Play](../../../../processes/marketing/churn-risk-play.md)
- **Watch What the Customer Does**
  - `ref/mkt/onboarding-email-program`, activity 10 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Watch What the Partner Does**
  - `ref/mkt/enable-channel-partner`, activity 14 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Watch the Transition**
  - `ref/mkt/pricing-change`, activity 14 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

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
