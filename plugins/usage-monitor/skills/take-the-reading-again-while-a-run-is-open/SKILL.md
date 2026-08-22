---
name: take-the-reading-again-while-a-run-is-open
description: Keeps a standing read open while an opening or a risk is being worked, so the evidence is current when somebody decides. Use it when running `ref/sls/open-an-expansion-deal` and `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Take the reading again while a run is open

## What it does

Keeps a standing read open while an opening or a risk is being worked,
so the evidence is current when somebody decides. Each read is taken
fresh at today's date and kept beside the earlier one rather than
replacing it.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Confirm the Opening Still Holds**
  - `ref/sls/open-an-expansion-deal`, activity 3 -
    [Open an Expansion Deal](../../../../processes/sales/open-an-expansion-deal.md)
- **Watch for the Signal to Turn**
  - `ref/sls/work-a-churn-risk`, activity 13 -
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
