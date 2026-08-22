---
name: brief-the-makers
description: Every agent hears the same play at once. Use it when running `ref/mkt/account-based-play`, `ref/mkt/customer-newsletter` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Brief the Makers

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/account-based-play`, every agent hears the same play at
  once
- in `ref/mkt/customer-newsletter`, everyone hears the same request at
  once
- in `ref/mkt/win-back-campaign`, everyone hears the offer and the
  segment at once

## Where it happens

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
