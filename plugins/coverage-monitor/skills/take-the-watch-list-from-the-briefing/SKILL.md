---
name: take-the-watch-list-from-the-briefing
description: Sits in the briefing that opens an audit, a study or an announcement and takes away what it is watching for, which sources it reads, and the dates its answer is due. Use it when running `ref/mkt/brand-audit` and `ref/mkt/brand-health`.
license: CC-BY-4.0
metadata:
  agent: coverage-monitor
  agent-version: "1"
---

# Take the watch list from the briefing

## What it does

Sits in the briefing that opens an audit, a study or an announcement and
takes away what it is watching for, which sources it reads, and the
dates its answer is due.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Brief the Audit**
  - `ref/mkt/brand-audit`, activity 4 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)
- **Brief the Wave**
  - `ref/mkt/brand-health`, activity 5 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)

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
