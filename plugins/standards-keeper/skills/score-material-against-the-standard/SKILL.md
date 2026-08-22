---
name: score-material-against-the-standard
description: Scores each item in a sample of material against the rule it has to meet, at the version of that rule which was in force, and records the verdict with the rule behind it. Use it when running `ref/mkt/brand-audit` and `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: standards-keeper
  agent-version: "1"
---

# Score material against the standard

## What it does

Scores each item in a sample of material against the rule it has to
meet, at the version of that rule which was in force, and records the
verdict with the rule behind it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Score the Pages against the Current Standards**
  - `ref/mkt/refresh-content`, activity 5 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Score the Sample**
  - `ref/mkt/brand-audit`, activity 7 -
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
