---
name: check-who-may-be-retargeted
description: The consent record says who may be advertised to. Use it when running `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Check Who May Be Retargeted

## What happens

The consent record says who may be advertised to.

## Where it happens

- `ref/mkt/display-retargeting`, activity 3 -
  [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)

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
