---
name: close-out-contacts-who-never-answered
description: Closes out the contacts that went through a whole run without ever answering, so they stop receiving messages. Use it when running `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Close out contacts who never answered

## What it does

Closes out the contacts that went through a whole run without ever
answering, so they stop receiving messages.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Retire the Ones Who Stayed Silent**
  - `ref/mkt/win-back-campaign`, activity 18 -
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
