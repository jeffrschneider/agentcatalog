---
name: hold-the-fund-through-the-period
description: Watches the balance as it is committed, moves money that will not be spent before the period closes and tells every partner the same thing on the same day when it does, and files what the period taught. Use it when running `ref/prt/allocate-the-fund`.
license: CC-BY-4.0
metadata:
  agent: fund-allocator
  agent-version: "1"
---

# Hold the fund through the period

## What it does

Watches the balance as it is committed, moves money that will not be
spent before the period closes and tells every partner the same thing on
the same day when it does, and files what the period taught.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Move Money That Will Not Be Used**
  - `ref/prt/allocate-the-fund`, activity 15 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Record What Was Learned**
  - `ref/prt/allocate-the-fund`, activity 17 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Watch the Fund as It Is Committed**
  - `ref/prt/allocate-the-fund`, activity 14 -
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
