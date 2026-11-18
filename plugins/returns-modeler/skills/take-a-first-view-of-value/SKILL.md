---
name: take-a-first-view-of-value
description: Builds a value range from the seller's numbers and comparable sales and listed companies, checks the fund's return at the low, middle and high of the range, sketches the equity, debt and rollover each price would need, and gives the indication of interest its range and its financing. Use it when running `ref/pc/respond-to-a-sale-process`.
license: CC-BY-4.0
metadata:
  agent: returns-modeler
  agent-version: "1"
---

# Take a first view of value

## What it does

Builds a value range from the seller's numbers and comparable sales and
listed companies, checks the fund's return at the low, middle and high
of the range, sketches the equity, debt and rollover each price would
need, and gives the indication of interest its range and its financing.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Build the First View of Value**
  - `ref/pc/respond-to-a-sale-process`, activity 10 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)
- **Check the Return at Each Price**
  - `ref/pc/respond-to-a-sale-process`, activity 11 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)
- **Sketch How It Would Be Paid For**
  - `ref/pc/respond-to-a-sale-process`, activity 12 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)
- **Write the Indication of Interest**
  - `ref/pc/respond-to-a-sale-process`, activity 15 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)

## What to record

Per first view: the value range with the comparables and assumptions
behind it, the return at the low, middle and high of the range against
the target, and the financing at each price with the equity, any debt,
any rollover and the fund's share, every seller's figure marked as the
seller's. Per model version: its date; the entry price and what it is a
multiple of, with its comparables; the structure; the later rounds and
their dilution, or the debt, its interest, its repayment and its
covenants, year by year; the four exit cases, each with an exit year, an
exit value and the source of its multiple; the multiple of money and the
IRR at each case, labeled gross, and net where the policy asks; the
sensitivities with the inputs that move the return most; the breakeven
and the exit value that returns the multiple the strategy needs; the
reserve against the fund's reserve plan; the assumption list with each
input's source, owner and date, and each unsourced input marked as the
deal team's assumption; the cases as the deal lead agreed them, with a
case moved without new evidence labeled as the deal lead's view; and
whom the version was handed to. The memo's returns at the model's
version. Per negotiation: the walk-away terms with the return at each,
each ask and each change priced for what it does to the return, the
ownership, the risk or the cash at closing, and the final return beside
the approval. Per company in trouble: each option's base and downside
return and its cost in ownership and money. Per exit: each route's
proceeds, multiple, IRR and time to cash beside the return from holding,
and the floor set for each route. An auditor can take any number in a
screen note, a memo, a term sheet or an exit paper and find the model
version, the case and the inputs behind it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
