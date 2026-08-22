---
name: decide-a-request-against-the-fund
description: Scores a request against the published eligible list, checks the balance is there, prices the organization's share with the match and the cap applied, decides it, holds the money against it, and records the decision with the reason it rests on. Use it when running `ref/prt/approve-a-fund-request`.
license: CC-BY-4.0
metadata:
  agent: fund-allocator
  agent-version: "1"
---

# Decide a request against the fund

## What it does

Scores a request against the published eligible list, checks the balance
is there, prices the organization's share with the match and the cap
applied, decides it, holds the money against it, and records the
decision with the reason it rests on.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Check the Activity Is Eligible**
  - `ref/prt/approve-a-fund-request`, activity 4 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Check the Money Is There**
  - `ref/prt/approve-a-fund-request`, activity 5 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Commit the Money**
  - `ref/prt/approve-a-fund-request`, activity 14 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Decide the Request**
  - `ref/prt/approve-a-fund-request`, activity 12 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Price the Organization's Share**
  - `ref/prt/approve-a-fund-request`, activity 10 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Record the Decision**
  - `ref/prt/approve-a-fund-request`, activity 17 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)

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
