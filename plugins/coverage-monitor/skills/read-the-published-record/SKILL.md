---
name: read-the-published-record
description: Reads back over what outlets, analysts and reviewers have already published about the organization and records each piece with where it ran, when it appeared, who wrote it and what it said. Use it when running `ref/mkt/brand-audit`, `ref/mkt/brand-health` and `ref/mkt/brief-industry-analyst`.
license: CC-BY-4.0
metadata:
  agent: coverage-monitor
  agent-version: "1"
---

# Read the published record

## What it does

Reads back over what outlets, analysts and reviewers have already
published about the organization and records each piece with where it
ran, when it appeared, who wrote it and what it said.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Read What Outsiders Published**
  - `ref/mkt/brand-audit`, activity 9 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)
- **Read What Was Published Outside**
  - `ref/mkt/brand-health`, activity 18 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
- **Read Where the Analyst Stands**
  - `ref/mkt/brief-industry-analyst`, activity 2 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)

## What to record

One entry per mention, giving the outlet, the date it appeared, the
author, the headline, the address it lives at, and what the piece said
about the organization, quoted where the exact wording matters. Each
entry says whether the mention can be traced back to something the
organization sent out. A summary at the cadence the process sets,
covering what ran, where it ran, and how the tone moved since the last
one. A source it could not reach appears in the summary as unreached.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
