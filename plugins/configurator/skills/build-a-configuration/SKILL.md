---
name: build-a-configuration
description: Turns an agreed shape into the products, the quantities and the term that can actually be sold and delivered, with a reason behind every option that is not the default. Use it when running `ref/sls/configure-and-price` and `ref/sls/respond-to-an-rfp`.
license: CC-BY-4.0
metadata:
  agent: configurator
  agent-version: "1"
---

# Build a configuration

## What it does

Turns an agreed shape into the products, the quantities and the term
that can actually be sold and delivered, with a reason behind every
option that is not the default. The same work supplies the lines a bid
is priced from and says how the work would be done.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Configuration**
  - `ref/sls/configure-and-price`, activity 3 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Design the Solution Response**
  - `ref/sls/respond-to-an-rfp`, activity 8 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Price the Bid**
  - `ref/sls/respond-to-an-rfp`, activity 9 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)

## What to record

Per run: the entitlement read, dated, with the contract each line came
from and the end date of each one. The configuration at a version, with
the reason behind every option that is not the default. The check result
naming each rule tested, each failure, and the rule behind any failure
that was accepted anyway. The quote check scored against the
configuration version and the rate card version it claims. The closing
record of what was configured, what it priced at, and what each approval
took. Somebody replaying the run can see why every line is in the
configuration and why it passed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
