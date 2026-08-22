---
name: assemble-a-quote-and-hand-it-on
description: Puts the priced lines, the quantities and the term together as one quote at one version, naming the card version behind every line and the date the offer stops being good. Use it when running `ref/sls/close-a-renewal`, `ref/sls/configure-and-price` and `ref/sls/write-a-proposal`.
license: CC-BY-4.0
metadata:
  agent: quote-builder
  agent-version: "1"
---

# Assemble a quote and hand it on

## What it does

Puts the priced lines, the quantities and the term together as one quote
at one version, naming the card version behind every line and the date
the offer stops being good. Hands it on to whoever writes the document
the buyer reads, and supplies the price and the terms as they appear
there.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Assemble the Quote**
  - `ref/sls/configure-and-price`, activity 11 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Build the Quote**
  - `ref/sls/close-a-renewal`, activity 6 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Hand the Quote On**
  - `ref/sls/configure-and-price`, activity 13 -
    [Configure and Price](../../../../processes/sales/configure-and-price.md)
- **Take in the Approved Quote**
  - `ref/sls/write-a-proposal`, activity 1 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)
- **Write the Price and the Terms**
  - `ref/sls/write-a-proposal`, activity 8 -
    [Write a Proposal](../../../../processes/sales/write-a-proposal.md)

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
