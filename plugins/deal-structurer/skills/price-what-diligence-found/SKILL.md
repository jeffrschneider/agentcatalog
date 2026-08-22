---
name: price-what-diligence-found
description: Takes in the diligence result and prices every finding into a term the agreement has to carry, or calls it a stop. Use it when running `ref/prt/run-alliance-diligence` and `ref/prt/structure-an-alliance`.
license: CC-BY-4.0
metadata:
  agent: deal-structurer
  agent-version: "1"
---

# Price what diligence found

## What it does

Takes in the diligence result and prices every finding into a term the
agreement has to carry, or calls it a stop. A finding that does not make
it into the paper is raised rather than dropped.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Decide What Each Finding Costs**
  - `ref/prt/run-alliance-diligence`, activity 16 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)
- **Take in the Diligence Result**
  - `ref/prt/structure-an-alliance`, activity 1 -
    [Structure an Alliance](../../../../processes/partners/structure-an-alliance.md)

## What to record

What each side must get, written before any shape was chosen. The shape
chosen and why it beat the others considered. The money model, naming
who charges the customer, who invoices whom, and who keeps what. The
term and the exit, with the notice each ending needs. The economics at a
version, with the assumptions and the downside case stated. Every
diligence finding, priced into a term or named as a stop. The internal
mandate and its walk-away terms. The term sheet at a version. Every ask
the other side made, the position taken on it, and the date it closed.
Every redline read against the term sheet, saying what moved and who was
told. The obligation register at handover, so the work the agreement
created has owners before anybody starts it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
