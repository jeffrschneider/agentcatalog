---
name: say-who-may-be-contacted
description: Applies the consent record to a named set of people or accounts and says which of them may be approached, on which channel, and where a study is involved, what may be asked of them. Use it when running `ref/mkt/account-based-play` and 7 other reference processes.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Say who may be contacted

## What it does

Applies the consent record to a named set of people or accounts and says
which of them may be approached, on which channel, and where a study is
involved, what may be asked of them.

## Where it happens

The agent does this in four activities across eight reference processes.
Each one names the activity as that process words it.

- **Check Who May Be Approached**
  - `ref/mkt/win-loss-analysis`, activity 6 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Check Who May Be Contacted**
  - `ref/mkt/account-based-play`, activity 6 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
  - `ref/mkt/brand-health`, activity 8 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 7 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
  - `ref/mkt/nurture-sequence`, activity 3 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Check Who May Be Retargeted**
  - `ref/mkt/display-retargeting`, activity 3 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Clear the Sample and the Questions**
  - `ref/mkt/buyer-persona`, activity 6 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
  - `ref/mkt/map-buyer-journey`, activity 5 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)

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
