---
name: rebuild-the-numbers-from-records
description: Ties revenue, cash and debt to the company's own invoices, contracts, accounts and bank statements, splits recurring revenue from one-off revenue, reads the margin and each cost line, and follows the cash, so every figure carries the record and the period it came from. Use it when running `ref/pc/collect-the-portfolio-company-reports`, `ref/pc/run-financial-diligence` and `ref/pc/write-the-value-creation-plan`.
license: CC-BY-4.0
metadata:
  agent: financial-analyst
  agent-version: "1"
---

# Rebuild the numbers from records

## What it does

Ties revenue, cash and debt to the company's own invoices, contracts,
accounts and bank statements, splits recurring revenue from one-off
revenue, reads the margin and each cost line, and follows the cash, so
every figure carries the record and the period it came from.

## Where it happens

The agent does this in seven activities across three reference
processes. Each one names the activity as that process words it.

- **Build the Baseline**
  - `ref/pc/write-the-value-creation-plan`, activity 2 -
    [Write the Value Creation Plan](../../../../processes/private-capital/write-the-value-creation-plan.md)
- **Follow the Cash**
  - `ref/pc/run-financial-diligence`, activity 8 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Margins and Costs**
  - `ref/pc/run-financial-diligence`, activity 7 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Rebuild the Revenue**
  - `ref/pc/run-financial-diligence`, activity 5 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Take in the Opportunity**
  - `ref/pc/run-financial-diligence`, activity 1 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Test the Quality of Revenue**
  - `ref/pc/run-financial-diligence`, activity 6 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Tie the Numbers to the Accounts**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 7 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)

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
