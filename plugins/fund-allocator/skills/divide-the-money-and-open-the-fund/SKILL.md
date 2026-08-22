---
name: divide-the-money-and-open-the-fund
description: Runs the rule against every partner, checks the amounts sum to the money that exists, opens the signed amounts on the books, and publishes the rule, the eligible list and the deadlines where every partner can read them. Use it when running `ref/prt/allocate-the-fund`.
license: CC-BY-4.0
metadata:
  agent: fund-allocator
  agent-version: "1"
---

# Divide the money and open the fund

## What it does

Runs the rule against every partner, checks the amounts sum to the money
that exists, opens the signed amounts on the books, and publishes the
rule, the eligible list and the deadlines where every partner can read
them. A partner can then work out its own number without asking anybody.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Amounts against the Money**
  - `ref/prt/allocate-the-fund`, activity 8 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Open the Fund on the Books**
  - `ref/prt/allocate-the-fund`, activity 11 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Publish the Rules Partners Can Read**
  - `ref/prt/allocate-the-fund`, activity 12 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Run the Rule against the Partners**
  - `ref/prt/allocate-the-fund`, activity 7 -
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
