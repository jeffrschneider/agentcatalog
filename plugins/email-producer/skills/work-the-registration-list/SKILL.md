---
name: work-the-registration-list
description: Chase, confirm, remind and manage the waitlist. Use it when running `ref/mkt/field-event` and `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Work the Registration List

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/field-event`, chase, confirm, remind and manage the
  waitlist
- in `ref/mkt/webinar`, confirm, remind, and chase the number needed

## Where it happens

- `ref/mkt/field-event`, activity 10 -
  [Host Field Event](../../../../processes/marketing/field-event.md)
- `ref/mkt/webinar`, activity 9 -
  [Produce Webinar](../../../../processes/marketing/webinar.md)

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
