---
name: record-the-assets
description: Opens each period's register, checks each purchase coded to an asset class against the capitalization policy and threshold, records each new asset with its class, cost, service date, useful life, location and owner, asks each owner to confirm it, takes in each disposal and transfer, and checks the register against what physically exists. Use it when running `ref/fin/account-for-fixed-assets`.
license: CC-BY-4.0
metadata:
  agent: asset-register-keeper
  agent-version: "1"
---

# Record the assets

## What it does

Opens each period's register, checks each purchase coded to an asset
class against the capitalization policy and threshold, records each new
asset with its class, cost, service date, useful life, location and
owner, asks each owner to confirm it, takes in each disposal and
transfer, and checks the register against what physically exists.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Check Each Cost Against the Policy**
  - `ref/fin/account-for-fixed-assets`, activity 3 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)
- **Check the Register Against What Exists**
  - `ref/fin/account-for-fixed-assets`, activity 7 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)
- **Confirm Each Asset With Its Owner**
  - `ref/fin/account-for-fixed-assets`, activity 5 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)
- **Open the Period's Register**
  - `ref/fin/account-for-fixed-assets`, activity 1 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)
- **Record Each New Asset**
  - `ref/fin/account-for-fixed-assets`, activity 4 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)
- **Take In Disposals and Transfers**
  - `ref/fin/account-for-fixed-assets`, activity 6 -
    [Account for Fixed Assets](../../../../processes/finance/account-for-fixed-assets.md)

## What to record

Each period leaves the register as it stood at the last close, each cost
read as an asset or an expense with the reason, each new asset with its
class, its cost, its service date, its useful life, its location and its
owner and the owner's confirmation, each disposal and transfer with the
owner's report and its evidence, and the result of each check against
what exists, with each asset marked found, missing, idle or damaged.
Beside them sit each disposal and impairment as set out with its
carrying value, any proceeds and its effect, the controller's decision
and any senior approval, each asset's depreciation for the period, the
reviewer's approval, the batch posted to the ledger, and the register
and its totals handed to the close. Each lease leaves the lease and
every document it names, its term, its payments and its options each
with the clause it came from, the lease owner's answer, each judgment
with its effect beside the controller's decision in writing, the lease
as entered at its version, the schedule, and each later period's entries
set to post. Nothing in the record shows this agent deciding a disposal,
an impairment or a judgment, or posting anything the reviewer has not
approved.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
