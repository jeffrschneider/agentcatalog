---
name: say-which-way-each-line-is-moving
description: Shows which parts of the customer started using what and when, which stopped, and the direction of travel on each line. Use it when running `ref/sls/spot-an-expansion` and `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Say which way each line is moving

## What it does

Shows which parts of the customer started using what and when, which
stopped, and the direction of travel on each line. A direction is read
over a window rather than off a single day.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Look for the Teams Newly Adopting**
  - `ref/sls/spot-an-expansion`, activity 5 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)
- **Read the Usage Trend**
  - `ref/sls/work-a-churn-risk`, activity 3 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)

## What to record

Per reading: the metered thing, the entitlement it is set against, the
periods compared, the system it was read from and the date it was read.
Per account: where use sits against each limit, which teams began using
what and when, which stopped and when, and the direction of travel on
each line. A reading is dated rather than reused, so a run that confirms
an opening or watches a risk turn records a fresh read at today's date
and keeps the earlier one beside it. Anyone auditing a decision can put
the reading next to the agreement and get the same answer.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
