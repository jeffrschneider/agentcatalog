---
name: keep-the-capital-accounts
description: Opens each investor's account at its commitment once the total is checked against the hard cap, reads what each investor has left to give, posts every call, charge and distribution to the accounts, and builds each investor's statement from its own account. Use it when running `ref/pc/allocate-fees-and-expenses` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: capital-account-keeper
  agent-version: "1"
---

# Keep the capital accounts

## What it does

Opens each investor's account at its commitment once the total is
checked against the hard cap, reads what each investor has left to give,
posts every call, charge and distribution to the accounts, and builds
each investor's statement from its own account.

## Where it happens

The agent does this in seven activities across five reference processes.
Each one names the activity as that process words it.

- **Build Each Investor's Statement**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 11 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)
- **Check the Total Against the Hard Cap**
  - `ref/pc/hold-a-fund-close`, activity 8 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Open Each Capital Account**
  - `ref/pc/hold-a-fund-close`, activity 11 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Post the Call to the Capital Accounts**
  - `ref/pc/issue-a-capital-call`, activity 15 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Post the Charges to the Capital Accounts**
  - `ref/pc/allocate-fees-and-expenses`, activity 17 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
- **Post the Distribution**
  - `ref/pc/make-a-distribution`, activity 16 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Read What Each Investor Has Left**
  - `ref/pc/issue-a-capital-call`, activity 3 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)

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
