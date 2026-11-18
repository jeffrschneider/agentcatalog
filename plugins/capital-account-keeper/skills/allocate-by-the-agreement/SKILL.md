---
name: allocate-by-the-agreement
description: "Splits every amount among the investors as the partnership agreement sets it: the later investors' true-up, each share of a call or a distribution summing to the cent, the amount to distribute, the waterfall and the carried interest with its holdback, the net asset value and the quarter's results. Use it when running `ref/pc/hold-a-fund-close` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: capital-account-keeper
  agent-version: "1"
---

# Allocate by the agreement

## What it does

Splits every amount among the investors as the partnership agreement
sets it: the later investors' true-up, each share of a call or a
distribution summing to the cent, the amount to distribute, the
waterfall and the carried interest with its holdback, the net asset
value and the quarter's results.

## Where it happens

The agent does this in eight activities across four reference processes.
Each one names the activity as that process words it.

- **Allocate the Quarter's Results**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 6 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)
- **Approve the True-Up**
  - `ref/pc/hold-a-fund-close`, activity 13 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Calculate the Later Investors' True-Up**
  - `ref/pc/hold-a-fund-close`, activity 12 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Run the Waterfall**
  - `ref/pc/make-a-distribution`, activity 5 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Set the Amount to Distribute**
  - `ref/pc/make-a-distribution`, activity 3 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Work Out Each Investor's Share**
  - `ref/pc/issue-a-capital-call`, activity 6 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
  - `ref/pc/make-a-distribution`, activity 6 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Work Out the Carried Interest**
  - `ref/pc/make-a-distribution`, activity 7 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Work Out the Net Asset Value**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 5 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)

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
