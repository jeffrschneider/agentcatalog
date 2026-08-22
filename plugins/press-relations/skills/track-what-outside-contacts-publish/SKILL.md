---
name: track-what-outside-contacts-publish
description: Reads what each outside contact has already published about the organization, logs whatever they publish afterwards, and reports what they now say against what the organization set out to have them say. Use it when running `ref/mkt/brief-industry-analyst`.
license: CC-BY-4.0
metadata:
  agent: press-relations
  agent-version: "1"
---

# Track what outside contacts publish

## What it does

Reads what each outside contact has already published about the
organization, logs whatever they publish afterwards, and reports what
they now say against what the organization set out to have them say.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Read Where the Analyst Stands**
  - `ref/mkt/brief-industry-analyst`, activity 2 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
- **Report Whether the Positioning Landed**
  - `ref/mkt/brief-industry-analyst`, activity 16 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
- **Watch What Gets Published**
  - `ref/mkt/brief-industry-analyst`, activity 14 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)

## What to record

A line for every contact, giving the date, the person, the material it
sent at its version, what that person asked, and what it gave them. The
contact record kept current, so anybody can see who covers this subject
and what they have already written. Every briefing with who attended,
what was shown, what was said under what terms, and what was promised
afterwards. The list of follow-ups it owes, each with the date it was
promised and the date it was delivered.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
