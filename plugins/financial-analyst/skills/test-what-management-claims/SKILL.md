---
name: test-what-management-claims
description: Accepts, cuts or leaves open each adjustment management proposes on its evidence, reads working capital and net debt, sets the forecast beside the company's past accuracy, records the tax adviser's view as the adviser's, reads the accountants' report against its own figures, and asks the company once for whatever is missing or does not tie. Use it when running `ref/pc/collect-the-portfolio-company-reports` and `ref/pc/run-financial-diligence`.
license: CC-BY-4.0
metadata:
  agent: financial-analyst
  agent-version: "1"
---

# Test what management claims

## What it does

Accepts, cuts or leaves open each adjustment management proposes on its
evidence, reads working capital and net debt, sets the forecast beside
the company's past accuracy, records the tax adviser's view as the
adviser's, reads the accountants' report against its own figures, and
asks the company once for whatever is missing or does not tie.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Ask the Company What Is Missing or Wrong**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 8 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Read Working Capital and Net Debt**
  - `ref/pc/run-financial-diligence`, activity 10 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Accountants' Report**
  - `ref/pc/run-financial-diligence`, activity 13 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Forecast**
  - `ref/pc/run-financial-diligence`, activity 11 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Tax Position**
  - `ref/pc/run-financial-diligence`, activity 12 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Test Management's Adjustments**
  - `ref/pc/run-financial-diligence`, activity 9 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)

## What to record

Per diligence run: every figure with the source document and the period
it was read from; the revenue tie-out period by period, with each gap
between revenue and cash; recurring and one-off revenue by customer,
product and cohort, with concentration, retention and price changes; the
margin and each cost line; the cash flow from the bank statements, the
burn, the runway and how much of the earnings became cash; each
adjustment accepted with the evidence that it will not recur, cut with
the years it did recur, or left open with its reason; the normal level
of working capital and every item counted as debt or as cash; the
forecast beside the company's past accuracy; the tax adviser's view
recorded as the adviser's; every difference with the accountants closed
or left open with both figures kept; each figure given without a record
marked as management's; and the agreed numbers at their version with the
deal lead's agreement. Per model: the operating case beside management's
plan with its assumptions, the rounds or the debt year by year, and the
second reading with each error found. Per value creation plan: the
baseline traced to source, each change sized for its value, cost and
time with its assumptions, a guess marked as a guess, and each progress
reading. Per period: each line tied or marked untied, any restatement
with the company's reason, the one list of questions with its date, each
variance over the threshold explained, the runway with undrawn
facilities and committed funding counted separately, and each covenant
calculated as the loan agreement defines it with its headroom and next
test date. An auditor can pick any number the fund relied on and follow
it to the record it came from, or find it marked as management's.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
