---
name: read-a-holding-against-its-plan
description: Reads each period's results against the budget, the value creation plan and the prior period, works out the months of cash left, and calculates each covenant as the loan agreement defines it with the headroom left. Use it when running `ref/pc/collect-the-portfolio-company-reports` and `ref/pc/write-the-value-creation-plan`.
license: CC-BY-4.0
metadata:
  agent: financial-analyst
  agent-version: "1"
---

# Read a holding against its plan

## What it does

Reads each period's results against the budget, the value creation plan
and the prior period, works out the months of cash left, and calculates
each covenant as the loan agreement defines it with the headroom left.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Read Progress Against the Plan**
  - `ref/pc/write-the-value-creation-plan`, activity 15 -
    [Write the Value Creation Plan](../../../../processes/private-capital/write-the-value-creation-plan.md)
- **Read the Results against Plan**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 9 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Test the Covenants**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 11 -
    [Collect the Portfolio Company Reports](../../../../processes/private-capital/collect-the-portfolio-company-reports.md)
- **Work Out the Cash Runway**
  - `ref/pc/collect-the-portfolio-company-reports`, activity 10 -
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
