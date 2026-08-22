---
name: check-it-holds-before-it-goes-out
description: Tests what was built against the product rules for missing dependencies, quantities under a minimum and options that cannot sit together, then scores the assembled quote against the configuration and the card version it claims to price. Use it when running `ref/sls/configure-and-price`.
license: CC-BY-4.0
metadata:
  agent: configurator
  agent-version: "1"
---

# Check it holds before it goes out

## What it does

Tests what was built against the product rules for missing dependencies,
quantities under a minimum and options that cannot sit together, then
scores the assembled quote against the configuration and the card
version it claims to price. A configuration that does not hold goes back
to be rebuilt rather than forward to be priced.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Configuration Holds**
  - `ref/sls/configure-and-price`, activity 4 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Check the Quote Before It Leaves**
  - `ref/sls/configure-and-price`, activity 12 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)

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
