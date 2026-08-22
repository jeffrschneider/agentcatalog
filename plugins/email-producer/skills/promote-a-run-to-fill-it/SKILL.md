---
name: promote-a-run-to-fill-it
description: Runs the messages that get people to sign up for something or turn up to it, pointed at registration or at where the thing is happening. Use it when running `ref/mkt/field-event` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Promote a run to fill it

## What it does

Runs the messages that get people to sign up for something or turn up to
it, pointed at registration or at where the thing is happening.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Promote the Conference**
  - `ref/mkt/user-conference`, activity 8 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Promote the Event**
  - `ref/mkt/field-event`, activity 9 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Promote the Presence**
  - `ref/mkt/trade-show`, activity 10 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Promote the Session**
  - `ref/mkt/webinar`, activity 8 -
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
