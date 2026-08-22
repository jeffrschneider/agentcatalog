---
name: take-the-send-from-the-briefing
description: "Sits in the briefing that starts a send and takes away the same account everyone else heard: who the message is for, what it has to say, what is changing, and when it has to arrive. Use it when running `ref/mkt/account-based-play` and 4 other reference processes."
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Take the send from the briefing

## What it does

Sits in the briefing that starts a send and takes away the same account
everyone else heard: who the message is for, what it has to say, what is
changing, and when it has to arrive.

## Where it happens

The agent does this in three activities across five reference processes.
Each one names the activity as that process words it.

- **Brief the Agents that Act**
  - `ref/mkt/onboarding-email-program`, activity 5 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Brief the Agents that Remake the Material**
  - `ref/mkt/brand-refresh`, activity 11 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Brief the Makers**
  - `ref/mkt/account-based-play`, activity 7 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
  - `ref/mkt/customer-newsletter`, activity 5 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
  - `ref/mkt/win-back-campaign`, activity 7 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

Each message at a version, with the proof record naming who was sent a
proof, when it went, and what they said. The audience at a version, with
the count before the consent, opt-out and suppression rules were
applied, the count after, and the rule behind every removal. The
schedule as it was set, including the send-time windows and any wait
between batches. The send record naming the version that went, the time
it fired, and the person who said go. The delivery report, with what was
delivered, what bounced hard, what bounced soft, who complained, who
unsubscribed, and who the sending system suppressed on its own. Anything
it could not verify before the send is recorded as unverified instead of
being left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
