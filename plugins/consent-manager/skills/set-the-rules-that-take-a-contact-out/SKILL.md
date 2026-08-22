---
name: set-the-rules-that-take-a-contact-out
description: Writes the rules that end a contact's run through a program and says where that contact goes next. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Set the rules that take a contact out

## What it does

Writes the rules that end a contact's run through a program and says
where that contact goes next.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Set the Exits**
  - `ref/mkt/nurture-sequence`, activity 5 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

## What to record

For every list it clears, the count it removed and the rule each removal
was made under. For every withdrawal, a dated line naming each system
that keeps a copy of the audience, when the withdrawal was written into
it, and when the write was confirmed. A verdict per item for a scored
change, each citing the rule and its version. For every send it stopped,
the rule the send would have broken and the contacts it would have
reached.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
