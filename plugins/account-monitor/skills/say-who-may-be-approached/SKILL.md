---
name: say-who-may-be-approached
description: The agent applies the stated criteria, the consent record and each account's standing to say which accounts may be approached, which have to be kept out and why, and which have agreed to be named. Use it when running `ref/mkt/advisory-board` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: account-monitor
  agent-version: "1"
---

# Say who may be approached

## What it does

The agent applies the stated criteria, the consent record and each
account's standing to say which accounts may be approached, which have
to be kept out and why, and which have agreed to be named.

## Where it happens

The agent does this in six activities across six reference processes.
Each one names the activity as that process words it.

- **Build the Suppression List**
  - `ref/mkt/display-retargeting`, activity 5 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Check Who May Be Approached**
  - `ref/mkt/win-loss-analysis`, activity 6 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Choose the Customers to Ask**
  - `ref/mkt/customer-reviews`, activity 4 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Get the Customer's Agreement**
  - `ref/mkt/award-entry`, activity 7 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
- **Read the Named Accounts**
  - `ref/mkt/win-back-campaign`, activity 2 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Settle the Membership**
  - `ref/mkt/advisory-board`, activity 3 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)

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
