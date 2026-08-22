---
name: send-the-step
description: The named owner says go and the send fires. Use it when running `ref/mkt/onboarding-email-program`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Send the Step

## What happens

The named owner says go and the send fires.

## Where it happens

- `ref/mkt/onboarding-email-program`, activity 9 -
  [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)

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
