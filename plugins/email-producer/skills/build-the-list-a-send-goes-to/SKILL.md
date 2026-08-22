---
name: build-the-list-a-send-goes-to
description: Builds the list a message goes to from the contacts that are eligible for it, with opt-outs and suppressions taken out, and splits it where each group has to get a different message. Use it when running `ref/mkt/field-event`, `ref/mkt/pricing-change` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Build the list a send goes to

## What it does

Builds the list a message goes to from the contacts that are eligible
for it, with opt-outs and suppressions taken out, and splits it where
each group has to get a different message.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Build the Contact List**
  - `ref/mkt/win-back-campaign`, activity 6 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Build the Invitation List**
  - `ref/mkt/field-event`, activity 5 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Build the Notice Lists**
  - `ref/mkt/pricing-change`, activity 9 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

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
