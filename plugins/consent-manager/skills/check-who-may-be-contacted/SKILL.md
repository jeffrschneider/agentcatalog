---
name: check-who-may-be-contacted
description: The consent record applied per account and channel. Use it when running `ref/mkt/account-based-play` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Check Who May Be Contacted

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/account-based-play`, the consent record applied per
  account and channel
- in `ref/mkt/brand-health`, the consent record applied to the drawn
  sample
- in `ref/mkt/customer-research`, the consent record applied to the
  drawn sample
- in `ref/mkt/nurture-sequence`, consent and suppression applied to the
  segment

## Where it happens

- `ref/mkt/account-based-play`, activity 6 -
  [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- `ref/mkt/brand-health`, activity 8 -
  [Measure Brand Health](../../../../processes/marketing/brand-health.md)
- `ref/mkt/customer-research`, activity 7 -
  [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- `ref/mkt/nurture-sequence`, activity 3 -
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
