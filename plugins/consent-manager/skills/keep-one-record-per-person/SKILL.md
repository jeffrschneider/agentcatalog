---
name: keep-one-record-per-person
description: Gathers opt-outs from every system that holds its own copy and merges duplicate records into one per person, keeping the strictest consent it finds. Use it when running `ref/mkt/contact-database-hygiene`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Keep one record per person

## What it does

Gathers opt-outs from every system that holds its own copy and merges
duplicate records into one per person, keeping the strictest consent it
finds.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Merge the Records**
  - `ref/mkt/contact-database-hygiene`, activity 8 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- **Reconcile the Consent Record**
  - `ref/mkt/contact-database-hygiene`, activity 5 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)

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
