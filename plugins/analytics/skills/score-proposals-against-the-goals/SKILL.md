---
name: score-proposals-against-the-goals
description: The agent scores each thing being put forward against the goals already set and the evidence behind it, and says how far each one would move those goals. Use it when running `ref/mkt/content-calendar` and `ref/mkt/prioritize-initiatives`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Score proposals against the goals

## What it does

The agent scores each thing being put forward against the goals already
set and the evidence behind it, and says how far each one would move
those goals.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Score the Candidates**
  - `ref/mkt/content-calendar`, activity 8 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Weigh the Requests against the Goals**
  - `ref/mkt/prioritize-initiatives`, activity 6 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
