---
name: apply-the-suppression
description: The suppression written into every list and system. Use it when running `ref/mkt/contact-database-hygiene` and `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Apply the Suppression

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/contact-database-hygiene`, the suppression written into
  every list and system
- in `ref/mkt/display-retargeting`, everyone on the list comes out of
  every pool

## Where it happens

- `ref/mkt/contact-database-hygiene`, activity 13 -
  [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- `ref/mkt/display-retargeting`, activity 8 -
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
