---
name: apply-consent-and-suppression
description: Everyone the consent record does not cover comes out. Use it when running `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Apply Consent and Suppression

## What happens

Everyone the consent record does not cover comes out.

## Where it happens

- `ref/mkt/target-audience-segment`, activity 9 -
  [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

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
