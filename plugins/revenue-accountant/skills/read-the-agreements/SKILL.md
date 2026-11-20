---
name: read-the-agreements
description: Opens the period with the schedule as last closed, reads each new or changed agreement through its booking for each thing promised, its price, its variable parts and when each is delivered, sets out each judgment it raises with the options and their effect, and sets each agreement's schedule from the decided judgments. Use it when running `ref/fin/recognize-revenue`.
license: CC-BY-4.0
metadata:
  agent: revenue-accountant
  agent-version: "1"
---

# Read the agreements

## What it does

Opens the period with the schedule as last closed, reads each new or
changed agreement through its booking for each thing promised, its
price, its variable parts and when each is delivered, sets out each
judgment it raises with the options and their effect, and sets each
agreement's schedule from the decided judgments.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Open the Period**
  - `ref/fin/recognize-revenue`, activity 1 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)
- **Read What Was Promised**
  - `ref/fin/recognize-revenue`, activity 3 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)
- **Set Out the Judgments**
  - `ref/fin/recognize-revenue`, activity 4 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)
- **Update the Revenue Schedule**
  - `ref/fin/recognize-revenue`, activity 6 -
    [Recognize Revenue](../../../../processes/finance/recognize-revenue.md)

## What to record

Each period leaves its dates, its entity and the schedule as it stood at
the last close, each new or changed agreement read for each thing
promised, its price, its variable parts and when each is delivered, each
judgment set out with its options and their effect beside the decision
in writing with the reason and the person who made it, and each
agreement's schedule at a version naming the decision behind each line.
Beside the schedule sit what each delivery owner confirmed with the
record that shows it, what was billed, each agreement's revenue for the
period with the deferred and unbilled amounts that follow, the entries
sent for posting with the approval and the posting behind them, and the
reconciliation of the deferred and the unbilled revenue with every
difference explained. The run closes with the revenue accounting lead's
review and the handover to the close. Nothing in the record shows this
agent deciding a judgment, posting an entry, or working out revenue from
a term nobody booked.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
