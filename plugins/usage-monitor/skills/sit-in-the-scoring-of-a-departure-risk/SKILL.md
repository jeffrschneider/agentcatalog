---
name: sit-in-the-scoring-of-a-departure-risk
description: Brings the usage reading to the assessment that scores how likely an account is to leave, alongside the other readings of the account. Use it when running `ref/sls/open-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Sit in the scoring of a departure risk

## What it does

Brings the usage reading to the assessment that scores how likely an
account is to leave, alongside the other readings of the account. Usage
alone is never the whole answer, and the agent does not score the risk
on its own.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Score the Risk of Leaving**
  - `ref/sls/open-a-renewal`, activity 7 -
    [Open a Renewal](../../../../processes/sales/open-a-renewal.md)

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
