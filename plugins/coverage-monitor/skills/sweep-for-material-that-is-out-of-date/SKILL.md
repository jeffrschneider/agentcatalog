---
name: sweep-for-material-that-is-out-of-date
description: Searches the places where material is published for anything that still carries something the organization has retired, and lists every hit with where it was found. Use it when running `ref/mkt/brand-refresh`.
license: CC-BY-4.0
metadata:
  agent: coverage-monitor
  agent-version: "1"
---

# Sweep for material that is out of date

## What it does

Searches the places where material is published for anything that still
carries something the organization has retired, and lists every hit with
where it was found.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Sweep for What Was Missed**
  - `ref/mkt/brand-refresh`, activity 22 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)

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
