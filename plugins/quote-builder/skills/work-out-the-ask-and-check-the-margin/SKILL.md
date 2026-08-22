---
name: work-out-the-ask-and-check-the-margin
description: Works out what discount is being asked for, line by line, with the evidence that sits behind it. Use it when running `ref/sls/configure-and-price` and `ref/sls/open-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: quote-builder
  agent-version: "1"
---

# Work out the ask and check the margin

## What it does

Works out what discount is being asked for, line by line, with the
evidence that sits behind it. Sets the price asked for against the least
that will be accepted, and sets the priced deal against the margin
floor.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Margin**
  - `ref/sls/configure-and-price`, activity 8 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Set the Ask and the Floor**
  - `ref/sls/open-a-renewal`, activity 9 -
    [Open a Renewal](../../../../processes/sales/open-a-renewal.md)
- **Work Out the Discount Ask**
  - `ref/sls/configure-and-price`, activity 7 -
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
