---
name: agree-and-hand-on-the-numbers
description: Agrees with the deal lead the figures the model and the price will use, each with its source and its adjustments, hands them to the model, the memo and the other diligence runs, and reads them into the model with their sources carried across. Use it when running `ref/pc/build-the-investment-model` and `ref/pc/run-financial-diligence`.
license: CC-BY-4.0
metadata:
  agent: financial-analyst
  agent-version: "1"
---

# Agree and hand on the numbers

## What it does

Agrees with the deal lead the figures the model and the price will use,
each with its source and its adjustments, hands them to the model, the
memo and the other diligence runs, and reads them into the model with
their sources carried across.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Numbers to Model From**
  - `ref/pc/run-financial-diligence`, activity 15 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Hand the Numbers On**
  - `ref/pc/run-financial-diligence`, activity 16 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Take in the Agreed Numbers**
  - `ref/pc/build-the-investment-model`, activity 1 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)

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
