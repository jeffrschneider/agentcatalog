---
name: charge-fees-and-expenses
description: Sets each period's fee basis, works out the management fee and the offsets from company fees, classifies every expense by the clause that allows it, splits the shared and broken-deal costs by the policy, tests the caps, and bills the firm and the companies for what they owe the fund. Use it when running `ref/pc/allocate-fees-and-expenses`.
license: CC-BY-4.0
metadata:
  agent: capital-account-keeper
  agent-version: "1"
---

# Charge fees and expenses

## What it does

Sets each period's fee basis, works out the management fee and the
offsets from company fees, classifies every expense by the clause that
allows it, splits the shared and broken-deal costs by the policy, tests
the caps, and bills the firm and the companies for what they owe the
fund.

## Where it happens

The agent does this in twelve activities across one reference process.
Each one names the activity as that process words it.

- **Allocate the Broken-Deal Costs**
  - `ref/pc/allocate-fees-and-expenses`, activity 10 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Bill What Others Owe the Fund**
  - `ref/pc/allocate-fees-and-expenses`, activity 18 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Check the Charges against the Caps**
  - `ref/pc/allocate-fees-and-expenses`, activity 11 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Classify Each Expense**
  - `ref/pc/allocate-fees-and-expenses`, activity 8 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Collect the Fees Paid by Companies**
  - `ref/pc/allocate-fees-and-expenses`, activity 5 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Gather the Period's Expenses**
  - `ref/pc/allocate-fees-and-expenses`, activity 7 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Open the Fee Period**
  - `ref/pc/allocate-fees-and-expenses`, activity 1 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Record What the Period Taught**
  - `ref/pc/allocate-fees-and-expenses`, activity 19 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Set the Fee Basis**
  - `ref/pc/allocate-fees-and-expenses`, activity 2 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Split the Shared Costs**
  - `ref/pc/allocate-fees-and-expenses`, activity 9 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Work Out the Fee Offsets**
  - `ref/pc/allocate-fees-and-expenses`, activity 6 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Work Out the Management Fee**
  - `ref/pc/allocate-fees-and-expenses`, activity 4 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)

## What to record

A close leaves the commitments set against the target and the hard cap
with the cut each investor would take, each new account opened at its
commitment with its side letter terms attached, and each later
investor's true-up with the interest charged and what each earlier
investor receives, beside the CFO's approval. A call leaves the clause
that allows it, each investor's unfunded commitment at a date, every
excused investor with the clause that excuses it, each share summing to
the call to the cent under the rounding rule, the notices at their
version, the contributions posted, and the reconciliation of called,
received and booked, investor by investor. A fee period leaves the basis
and the rate, the side letter terms applied, each investor's fee to the
cent, every company fee and its offset, every expense with the clause
that lets the fund carry it or classed as the firm's, the shared and
broken-deal splits, the caps tested with the running total, and the
bills raised. A distribution leaves the cleared proceeds, the amount
kept back, the character of each part, the waterfall tier by tier, each
investor's share, the carried interest with its holdback and the running
clawback test, the tax withheld for each investor, and the
reconciliation of approved, paid, withheld and booked. Each quarter
leaves the closed books, the net asset value, the quarter's results
allocated with the accrued carry, and each investor's statement built
from its own account. Each year leaves the auditor's request log, the
statements at each draft, the support for every sampled amount traced to
its notice, its bank record and its clause, the settled findings, each
investor's tax share and status, and every estimate marked as an
estimate. Beside every amount sits the independent working that agrees
with it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
