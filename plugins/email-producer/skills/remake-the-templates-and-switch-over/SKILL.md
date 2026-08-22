---
name: remake-the-templates-and-switch-over
description: Remakes the templates that messages and pages are built from, stages the new versions where they can be previewed without serving anyone, and switches the properties and the sending system over on the agreed day. Use it when running `ref/mkt/brand-refresh`.
license: CC-BY-4.0
metadata:
  agent: email-producer
  agent-version: "1"
---

# Remake the templates and switch over

## What it does

Remakes the templates that messages and pages are built from, stages the
new versions where they can be previewed without serving anyone, and
switches the properties and the sending system over on the agreed day.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Rebuild the Templates**
  - `ref/mkt/brand-refresh`, activity 12 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Stage the Changes**
  - `ref/mkt/brand-refresh`, activity 18 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Switch the Properties**
  - `ref/mkt/brand-refresh`, activity 19 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)

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
