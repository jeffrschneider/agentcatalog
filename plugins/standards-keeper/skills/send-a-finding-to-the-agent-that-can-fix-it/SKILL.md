---
name: send-a-finding-to-the-agent-that-can-fix-it
description: Sends each finding to the agent that can close it, and sends a rule or a claim that no longer holds back to be written again. Use it when running `ref/mkt/brand-audit` and `ref/mkt/competitive-battlecard`.
license: CC-BY-4.0
metadata:
  agent: standards-keeper
  agent-version: "1"
---

# Send a finding to the agent that can fix it

## What it does

Sends each finding to the agent that can close it, and sends a rule or a
claim that no longer holds back to be written again.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand on the Claim Change**
  - `ref/mkt/competitive-battlecard`, activity 15 -
    [Refresh Competitive Battlecard](../../../../processes/marketing/competitive-battlecard.md)
- **Hand the Gaps to the Owners**
  - `ref/mkt/brand-audit`, activity 16 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)

## What to record

Every standard at a numbered version, with the date it took effect and
the date it stopped being current. A change record for each version,
saying what changed, what it replaced, who approved it, and when. Every
earlier version left readable at its own number, so work can be judged
against the standard it was made under. Every interpretation it issued,
attached to the rule and the version it interprets, carrying the
question that prompted it and the agent that asked. A dated record of
who was told about each change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
