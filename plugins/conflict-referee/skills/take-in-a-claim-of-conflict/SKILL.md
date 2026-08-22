---
name: take-in-a-claim-of-conflict
description: Takes in a claim that two sides are on the same customer, records what the claimant says the rule gives them, and checks what is already registered against that customer before anything else is read. Use it when running `ref/prt/register-a-deal` and `ref/prt/resolve-a-channel-conflict`.
license: CC-BY-4.0
metadata:
  agent: conflict-referee
  agent-version: "1"
---

# Take in a claim of conflict

## What it does

Takes in a claim that two sides are on the same customer, records what
the claimant says the rule gives them, and checks what is already
registered against that customer before anything else is read.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check for an Existing Claim**
  - `ref/prt/register-a-deal`, activity 4 -
    [Register a Deal](../../../../processes/partners/register-a-deal.md)
- **Take in the Claim of Conflict**
  - `ref/prt/resolve-a-channel-conflict`, activity 1 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)

## What to record

Who raised it, on which deal, and what they said the rule gives them.
The stop, with the time each side confirmed it rather than being assumed
to have. The single account both deals point at, or the finding that
they are two customers. The rule at the version in force on the claim
date, and the clauses the case turns on. Who was first on the dated
record, and by how much. The introduction marked evidenced, asserted or
absent. Each side's account as given, and every place it disagrees with
the record. The decision with the clause behind it and every fact it
cites, the earlier decisions checked, any departure said in writing, and
the signer. The one text both sides received and the date they received
it. Which side picked the deal up, and what the customer was told.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
