---
name: read-use-against-what-was-bought
description: "Sets what the customer actually used against the entitlement on the agreement, period by period, and reports the gap in both directions: the metered thing running past its limit, and the entitlement nobody is touching. Use it when running `ref/fin/issue-a-customer-invoice` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: usage-monitor
  agent-version: "1"
---

# Read use against what was bought

## What it does

Sets what the customer actually used against the entitlement on the
agreement, period by period, and reports the gap in both directions: the
metered thing running past its limit, and the entitlement nobody is
touching. The same reading answers what a customer says about their own
use, and gives each metered item's usage for a billing period to an
invoice billed on use.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Check What They Say Against Use**
  - `ref/sls/close-a-renewal`, activity 4 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Measure What Was Used**
  - `ref/sls/open-a-renewal`, activity 4 -
    [Open a Renewal](../../../../processes/sales/open-a-renewal.md)
- **Read the Metered Usage**
  - `ref/fin/issue-a-customer-invoice`, activity 3 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)
- **Read the Usage Against the Limit**
  - `ref/sls/spot-an-expansion`, activity 4 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)

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
