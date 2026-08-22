---
name: take-in-a-finished-definition
description: Takes in a definition another agent has finished and says what it changes about how messages are built and who they go to. Use it when running `ref/mkt/buyer-persona`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Take in a finished definition

## What it does

Takes in a definition another agent has finished and says what it
changes about how messages are built and who they go to.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Hand over the Persona**
  - `ref/mkt/buyer-persona`, activity 18 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)

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
