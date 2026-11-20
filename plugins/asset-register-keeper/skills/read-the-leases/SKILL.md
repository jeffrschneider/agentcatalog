---
name: read-the-leases
description: Takes in each signed or changed lease with every document it names, reads its term, its payments and its options each with the clause it came from, asks the lease owner how the business means to use the asset and each option, and enters the lease in the register with the decided judgments. Use it when running `ref/fin/account-for-a-lease`.
license: CC-BY-4.0
metadata:
  agent: asset-register-keeper
  agent-version: "1"
---

# Read the leases

## What it does

Takes in each signed or changed lease with every document it names,
reads its term, its payments and its options each with the clause it
came from, asks the lease owner how the business means to use the asset
and each option, and enters the lease in the register with the decided
judgments.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Ask the Lease Owner**
  - `ref/fin/account-for-a-lease`, activity 4 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)
- **Enter the Lease in the Register**
  - `ref/fin/account-for-a-lease`, activity 7 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)
- **Read the Options**
  - `ref/fin/account-for-a-lease`, activity 3 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)
- **Read the Term and the Payments**
  - `ref/fin/account-for-a-lease`, activity 2 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)
- **Take In the Lease**
  - `ref/fin/account-for-a-lease`, activity 1 -
    [Account for a Lease](../../../../processes/finance/account-for-a-lease.md)

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
