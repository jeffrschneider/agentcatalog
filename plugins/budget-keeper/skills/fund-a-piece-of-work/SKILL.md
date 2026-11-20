---
name: fund-a-piece-of-work
description: The agent sets money aside for a named piece of work, such as a purchase order, against the allocation it comes from, records the cap and the term it runs under, says whether that allocation still holds enough to cover it, and releases what is left once the work closes or is cancelled. Use it when running `ref/fin/issue-a-purchase-order` and 7 other reference processes.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Fund a piece of work

## What it does

The agent sets money aside for a named piece of work, such as a purchase
order, against the allocation it comes from, records the cap and the
term it runs under, says whether that allocation still holds enough to
cover it, and releases what is left once the work closes or is
cancelled.

## Where it happens

The agent does this in nine activities across eight reference processes.
Each one names the activity as that process words it.

- **Check the Budget Line Has Room**
  - `ref/fin/issue-a-purchase-order`, activity 3 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Close the Order**
  - `ref/fin/issue-a-purchase-order`, activity 15 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Commission the New Capacity**
  - `ref/mkt/plan-marketing-capacity`, activity 14 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Cover What It Costs**
  - `ref/mkt/win-loss-analysis`, activity 8 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Cover the Cost**
  - `ref/mkt/brand-health`, activity 10 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 9 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Record the Commitment**
  - `ref/fin/issue-a-purchase-order`, activity 10 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Resource the Commitments**
  - `ref/mkt/prioritize-initiatives`, activity 11 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Secure the Name**
  - `ref/mkt/name-product`, activity 13 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Set the Budget and the Term**
  - `ref/mkt/engage-marketing-agency`, activity 5 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)

## What to record

It leaves the budget at a version for the year, with one line per
function carrying what was allocated, what was already committed against
it before the year began, what has been drawn, and what is left. Every
change to an allocation goes in as a new version naming who approved it,
on what date, and which line the money moved from and to, and the
version it replaces stays where it was. Every draw is recorded against
the allocation it came from and the run that made it. The uncommitted
remainder is restated whenever a draw or a change lands. Once the
reconciliation for a period closes, that period's figures are frozen, so
a question about it a year later gets the same answer it got on the day.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
