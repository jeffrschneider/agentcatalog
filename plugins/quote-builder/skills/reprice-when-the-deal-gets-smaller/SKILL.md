---
name: reprice-when-the-deal-gets-smaller
description: Prices a smaller term again and sends it back through approval. Use it when running `ref/sls/close-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: quote-builder
  agent-version: "1"
---

# Reprice when the deal gets smaller

## What it does

Prices a smaller term again and sends it back through approval. The new
price and its distance from the floor are recorded beside the old one
rather than in place of it.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Reprice a Smaller Term**
  - `ref/sls/close-a-renewal`, activity 10 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)

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
