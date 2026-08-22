---
name: record-what-was-configured-and-priced
description: Closes a pricing run on the record with the configuration at its version, the card version behind it, and what each approval took, so somebody replaying the run can see why every line is there. Use it when running `ref/sls/configure-and-price`.
license: CC-BY-4.0
metadata:
  agent: configurator
  agent-version: "1"
---

# Record what was configured and priced

## What it does

Closes a pricing run on the record with the configuration at its
version, the card version behind it, and what each approval took, so
somebody replaying the run can see why every line is there.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Record What Was Priced**
  - `ref/sls/configure-and-price`, activity 14 -
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
