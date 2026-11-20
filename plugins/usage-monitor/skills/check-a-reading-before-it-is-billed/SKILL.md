---
name: check-a-reading-before-it-is-billed
description: Checks that a reading covers the whole billing period and reconciles with the meter and with what was billed before, and holds a reading that is missing, broken or for the wrong period with its reason, so no invoice goes out on it. Use it when running `ref/fin/issue-a-customer-invoice`.
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Check a reading before it is billed

## What it does

Checks that a reading covers the whole billing period and reconciles
with the meter and with what was billed before, and holds a reading that
is missing, broken or for the wrong period with its reason, so no
invoice goes out on it.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check the Usage Reading Is Complete**
  - `ref/fin/issue-a-customer-invoice`, activity 4 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)

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
