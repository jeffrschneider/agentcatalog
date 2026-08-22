---
name: read-what-the-customer-already-owns
description: Reads the contracts and entitlements already in force before anything is added, with the end date on each one, so nothing the customer already pays for is sold to them twice. Use it when running `ref/sls/configure-and-price`.
license: CC-BY-4.0
metadata:
  agent: configurator
  agent-version: "1"
---

# Read what the customer already owns

## What it does

Reads the contracts and entitlements already in force before anything is
added, with the end date on each one, so nothing the customer already
pays for is sold to them twice.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Read What the Customer Owns**
  - `ref/sls/configure-and-price`, activity 2 -
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
