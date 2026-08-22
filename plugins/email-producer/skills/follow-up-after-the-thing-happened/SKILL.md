---
name: follow-up-after-the-thing-happened
description: "Sends people what they were promised after they came: the recording, the material, the answers to what was asked, and what happens next. Use it when running `ref/mkt/advisory-board`, `ref/mkt/field-event` and `ref/mkt/webinar`."
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Follow up after the thing happened

## What it does

Sends people what they were promised after they came: the recording, the
material, the answers to what was asked, and what happens next.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Follow up with the Members**
  - `ref/mkt/advisory-board`, activity 15 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)
- **Follow up with the People Who Came**
  - `ref/mkt/field-event`, activity 14 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Follow up with the Registrants**
  - `ref/mkt/webinar`, activity 15 -
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
