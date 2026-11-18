---
name: issue-the-model-and-write-its-returns
description: Has the deal lead agree the cases, locks and issues the model at a version, hands it to the mandate check, the memo and the term sheet, and writes the memo's returns and proposed terms from that version alone. Use it when running `ref/pc/build-the-investment-model` and `ref/pc/write-the-investment-memo`.
license: CC-BY-4.0
metadata:
  agent: returns-modeler
  agent-version: "1"
---

# Issue the model and write its returns

## What it does

Has the deal lead agree the cases, locks and issues the model at a
version, hands it to the mandate check, the memo and the term sheet, and
writes the memo's returns and proposed terms from that version alone.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Cases**
  - `ref/pc/build-the-investment-model`, activity 15 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)
- **Hand the Model On**
  - `ref/pc/build-the-investment-model`, activity 17 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)
- **Issue the Model at a Version**
  - `ref/pc/build-the-investment-model`, activity 16 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)
- **Write the Proposed Terms**
  - `ref/pc/write-the-investment-memo`, activity 9 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Returns**
  - `ref/pc/write-the-investment-memo`, activity 8 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)

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
