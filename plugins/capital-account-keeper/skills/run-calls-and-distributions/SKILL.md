---
name: run-calls-and-distributions
description: Takes in a call request or cleared proceeds, checks a call is allowed and takes out the excused investors, drafts one notice per investor, chases a late payer with investor relations, hands the cash to its use, and reconciles each call and distribution to the cent. Use it when running `ref/pc/issue-a-capital-call` and `ref/pc/make-a-distribution`.
license: CC-BY-4.0
metadata:
  agent: capital-account-keeper
  agent-version: "1"
---

# Run calls and distributions

## What it does

Takes in a call request or cleared proceeds, checks a call is allowed
and takes out the excused investors, drafts one notice per investor,
chases a late payer with investor relations, hands the cash to its use,
and reconciles each call and distribution to the cent.

## Where it happens

The agent does this in twelve activities across two reference processes.
Each one names the activity as that process words it.

- **Chase a Late or Short Payment**
  - `ref/pc/issue-a-capital-call`, activity 13 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Check the Call Is Allowed**
  - `ref/pc/issue-a-capital-call`, activity 2 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Draft the Distribution Notices**
  - `ref/pc/make-a-distribution`, activity 11 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Draft the Notices**
  - `ref/pc/issue-a-capital-call`, activity 8 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Hand the Cash to Its Use**
  - `ref/pc/issue-a-capital-call`, activity 17 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Reconcile the Call**
  - `ref/pc/issue-a-capital-call`, activity 16 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Reconcile the Distribution**
  - `ref/pc/make-a-distribution`, activity 17 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Record What the Call Taught**
  - `ref/pc/issue-a-capital-call`, activity 18 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Record What the Run Taught**
  - `ref/pc/make-a-distribution`, activity 18 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Take Out the Excused Investors**
  - `ref/pc/issue-a-capital-call`, activity 4 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Take in the Call Request**
  - `ref/pc/issue-a-capital-call`, activity 1 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Take in the Proceeds**
  - `ref/pc/make-a-distribution`, activity 1 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)

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
