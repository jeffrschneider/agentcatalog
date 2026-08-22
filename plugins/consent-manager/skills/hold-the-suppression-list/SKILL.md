---
name: hold-the-suppression-list
description: Keeps the list of people who must never be reached, with a reason against each entry, and writes it into every list and system that sends. Use it when running `ref/mkt/contact-database-hygiene` and `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Hold the suppression list

## What it does

Keeps the list of people who must never be reached, with a reason
against each entry, and writes it into every list and system that sends.
Afterwards it reads what was delivered and confirms that nobody the list
took out was reached anyway.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Apply the Suppression**
  - `ref/mkt/contact-database-hygiene`, activity 13 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
  - `ref/mkt/display-retargeting`, activity 8 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Build the Suppression List**
  - `ref/mkt/display-retargeting`, activity 5 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Check the Suppression Is Holding**
  - `ref/mkt/display-retargeting`, activity 15 -
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
