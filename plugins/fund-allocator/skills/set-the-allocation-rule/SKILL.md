---
name: set-the-allocation-rule
description: Takes in the approved budget, reads what last period's fund did, and settles the rule the money will be divided by. Use it when running `ref/prt/allocate-the-fund`.
license: CC-BY-4.0
metadata:
  agent: fund-allocator
  agent-version: "1"
---

# Set the allocation rule

## What it does

Takes in the approved budget, reads what last period's fund did, and
settles the rule the money will be divided by. It says which activities
the fund may buy and which it may not, and sets the caps, the share each
side pays and any pool held back.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Choose the Allocation Rule**
  - `ref/prt/allocate-the-fund`, activity 4 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Read Last Period's Fund**
  - `ref/prt/allocate-the-fund`, activity 2 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Set What the Fund May Buy**
  - `ref/prt/allocate-the-fund`, activity 5 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Set the Caps, the Match and the Pool**
  - `ref/prt/allocate-the-fund`, activity 6 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Take in the Approved Budget**
  - `ref/prt/allocate-the-fund`, activity 1 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)

## What to record

The allocation rule at a version, with the date it was published and the
date every partner was told. Per partner, the amount and the exact
inputs the rule read to produce it. The eligible activity list at a
version, saying what is excluded as well as what is included. The
amounts summed against the approved budget, and the difference. Per
request: the eligibility finding naming the list version it was scored
against, the balance at the time, the organization's share with the
match and the cap applied, the decision and the reason it rests on. Per
commitment: the amount held, the partner's fund it came from, and the
date it expires. Per release: what went back to the fund and why. At the
period close, what was allocated, committed, claimed, paid, released and
moved. Any auditor can recompute a partner's allocation from the rule
version and the recorded inputs.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
