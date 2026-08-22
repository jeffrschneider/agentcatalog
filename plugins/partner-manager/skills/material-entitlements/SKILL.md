---
name: material-entitlements
description: Says which material a partner is allowed to see, working from the tier they sit in and the terms of their agreement, and records which version each tier is given. Use it when running `ref/mkt/competitive-battlecard` and `ref/mkt/enable-channel-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-manager
  agent-version: "1"
---

# Material entitlements

## What it does

Says which material a partner is allowed to see, working from the tier
they sit in and the terms of their agreement, and records which version
each tier is given.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Decide What the Partner May See**
  - `ref/mkt/enable-channel-partner`, activity 5 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Say What Partners May See**
  - `ref/mkt/competitive-battlecard`, activity 16 -
    [Refresh Competitive Battlecard](../../../../processes/marketing/competitive-battlecard.md)

## What to record

The partner record at a version, naming the agreement it rests on, the
tier the partner holds, the date that tier was set and who set it. For
everything the partner was given, the version it was at and the date it
went to them. For every person the partner put through training, what
they were trained on and the date they finished. A dated line for each
obligation as it comes due, saying whether it was met and by whom. What
the partner delivered back, counted against what the agreement asked
for, at the cadence the process sets. The CONVENED and DONE records of
everything it convenes, and the approval record behind every release and
every tier change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
