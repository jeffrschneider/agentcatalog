---
name: read-what-a-partner-delivered
description: "Pulls the same measures, over the same period, from the same sources for every partner: the deals and registrations they brought and what became of them, what a funded activity actually produced, what the partnership did last year, and what moved on the accounts a plan named. Use it when running `ref/prt/allocate-the-fund` and 6 other reference processes."
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Read what a partner delivered

## What it does

Pulls the same measures, over the same period, from the same sources for
every partner: the deals and registrations they brought and what became
of them, what a funded activity actually produced, what the partnership
did last year, and what moved on the accounts a plan named. Every
reading names its measure set at a version and the date each number was
pulled, so somebody else can recompute it.

## Where it happens

The agent does this in seven activities across seven reference
processes. Each one names the activity as that process words it.

- **Check What the Activity Produced**
  - `ref/prt/check-and-pay-a-claim`, activity 7 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Gather What the Partner Delivered**
  - `ref/prt/review-partner-performance`, activity 3 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)
- **Pull the Same Evidence for Everybody**
  - `ref/prt/set-a-partner-tier`, activity 3 -
    [Set a Partner Tier](../../../../processes/partners/set-a-partner-tier.md)
- **Read Last Year**
  - `ref/prt/write-a-joint-plan`, activity 2 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)
- **Read What Each Partner Delivered**
  - `ref/prt/allocate-the-fund`, activity 3 -
    [Allocate the Fund](../../../../processes/partners/allocate-the-fund.md)
- **Read What the Partner Did Before**
  - `ref/prt/approve-a-fund-request`, activity 6 -
    [Approve a Fund Request](../../../../processes/partners/approve-a-fund-request.md)
- **Read the Accounts**
  - `ref/prt/review-a-joint-plan`, activity 6 -
    [Review a Joint Plan](../../../../processes/partners/review-a-joint-plan.md)

## What to record

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
