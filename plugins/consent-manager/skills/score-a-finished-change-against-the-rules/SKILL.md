---
name: score-a-finished-change-against-the-rules
description: Names the consent and retention rules at the versions that apply before any scoring starts, then scores every item in a finished change or list against them and cites the rule behind each removal. Use it when running `ref/mkt/contact-database-hygiene` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Score a finished change against the rules

## What it does

Names the consent and retention rules at the versions that apply before
any scoring starts, then scores every item in a finished change or list
against them and cites the rule behind each removal.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Rules in Force**
  - `ref/mkt/contact-database-hygiene`, activity 3 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
  - `ref/mkt/target-audience-segment`, activity 2 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Score the Finished Change**
  - `ref/mkt/contact-database-hygiene`, activity 15 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- **Score the Finished List**
  - `ref/mkt/target-audience-segment`, activity 11 -
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
