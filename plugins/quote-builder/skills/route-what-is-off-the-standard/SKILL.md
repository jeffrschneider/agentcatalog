---
name: route-what-is-off-the-standard
description: Names anything off the standard price or the standard paper and puts it to the people who may sign it, before the quote exists rather than after it is sent. Use it when running `ref/sls/close-a-renewal`, `ref/sls/configure-and-price` and `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: quote-builder
  agent-version: "1"
---

# Route what is off the standard

## What it does

Names anything off the standard price or the standard paper and puts it
to the people who may sign it, before the quote exists rather than after
it is sent. A signature covers a version, so a quote changed afterwards
goes back through.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Approve What Is Off the Standard**
  - `ref/sls/close-a-renewal`, activity 7 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Get the Cost Approved**
  - `ref/sls/work-a-churn-risk`, activity 10 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)
- **Route the Non-Standard Terms**
  - `ref/sls/configure-and-price`, activity 9 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)

## What to record

Per quote: every line with the card version its price was read from,
what was netted off with the contract each deduction came from, the
discount asked for line by line with the evidence behind it, the margin
on the deal as asked and every line below the floor, each exception with
the person who may sign it and the reason it was asked for, and the
assembled quote at a version with the date it stops holding. When a term
is repriced smaller, the new price and its distance from the floor are
recorded beside the old one rather than replacing it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
