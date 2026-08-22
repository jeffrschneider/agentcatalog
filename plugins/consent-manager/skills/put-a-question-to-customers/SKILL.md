---
name: put-a-question-to-customers
description: Puts an approved question to customers who may be contacted and brings back what they said. Use it when running `ref/mkt/brand-audit`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Put a question to customers

## What it does

Puts an approved question to customers who may be contacted and brings
back what they said.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Ask the Audience**
  - `ref/mkt/brand-audit`, activity 10 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)

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
