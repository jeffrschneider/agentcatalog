---
name: tell-the-agents-that-read-a-standard-what-changed
description: Tells every agent and process that reads a standard that a new version is in force, what changed in it, and from when, and records that each one confirmed it has the new version. Use it when running `ref/mkt/attribution-model` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: standards-keeper
  agent-version: "1"
---

# Tell the agents that read a standard what changed

## What it does

Tells every agent and process that reads a standard that a new version
is in force, what changed in it, and from when, and records that each
one confirmed it has the new version.

## Where it happens

The agent does this in four activities across seven reference processes.
Each one names the activity as that process words it.

- **Hand the Decisions On**
  - `ref/mkt/brief-executive-leadership`, activity 19 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Tell Everyone Who Works to the Brand**
  - `ref/mkt/brand-guidelines`, activity 14 -
    [Publish Brand Guidelines](../../../../processes/marketing/brand-guidelines.md)
- **Tell the Processes that Read It**
  - `ref/mkt/brand-positioning`, activity 15 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
  - `ref/mkt/brand-refresh`, activity 3 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
  - `ref/mkt/brand-voice`, activity 16 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
  - `ref/mkt/name-product`, activity 15 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Tell the Processes that Read the Model**
  - `ref/mkt/attribution-model`, activity 14 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

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
