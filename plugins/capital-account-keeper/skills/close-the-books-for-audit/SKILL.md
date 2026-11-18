---
name: close-the-books-for-audit
description: Closes the quarter's and the year's books, drafts the fund's financial statements, answers every auditor request from the books in one log, supports the capital accounts and fees, gets the cash and the holdings confirmed, and works the auditor's findings with the chief financial officer. Use it when running `ref/pc/close-the-year-end-audit-and-tax-documents` and `ref/pc/issue-the-quarterly-report-and-statements`.
license: CC-BY-4.0
metadata:
  agent: capital-account-keeper
  agent-version: "1"
---

# Close the books for audit

## What it does

Closes the quarter's and the year's books, drafts the fund's financial
statements, answers every auditor request from the books in one log,
supports the capital accounts and fees, gets the cash and the holdings
confirmed, and works the auditor's findings with the chief financial
officer.

## Where it happens

The agent does this in nine activities across two reference processes.
Each one names the activity as that process words it.

- **Answer the Auditor's Requests**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 4 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Close the Quarter's Books**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 4 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)
- **Close the Year's Books**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 2 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Confirm the Cash and the Holdings**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 7 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Draft the Financial Statements**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 3 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Open the Year-End Close**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 1 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Record What the Year Taught**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 19 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Settle the Auditor's Findings**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 8 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Support the Capital Accounts and Fees**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 6 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)

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
