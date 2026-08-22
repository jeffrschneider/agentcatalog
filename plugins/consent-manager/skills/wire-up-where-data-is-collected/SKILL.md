---
name: wire-up-where-data-is-collected
description: "Sets up the places data is collected so they only collect where consent covers it: the tag on the site, the form fields, the tracking, and where each record goes once it is taken. Use it when running `ref/mkt/co-marketing-campaign` and `ref/mkt/display-retargeting`."
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Wire up where data is collected

## What it does

Sets up the places data is collected so they only collect where consent
covers it: the tag on the site, the form fields, the tracking, and where
each record goes once it is taken.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Tag the Site**
  - `ref/mkt/display-retargeting`, activity 6 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Wire up the Split**
  - `ref/mkt/co-marketing-campaign`, activity 10 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)

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
