---
name: hand-the-findings-to-the-agents-that-act
description: The agent puts the findings in front of the agents that will act on them before the findings issue, and records what each one says it will change and who owns it from there. Use it when running `ref/mkt/analyze-customer-base` and `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Hand the findings to the agents that act

## What it does

The agent puts the findings in front of the agents that will act on them
before the findings issue, and records what each one says it will change
and who owns it from there.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Hand It to the Owner**
  - `ref/mkt/select-marketing-technology`, activity 20 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Hand over the Findings**
  - `ref/mkt/analyze-customer-base`, activity 17 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Review the Findings**
  - `ref/mkt/analyze-customer-base`, activity 15 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
