---
name: establish-the-facts
description: Builds the record the decision will rest on. Use it when running `ref/prt/resolve-a-channel-conflict`.
license: CC-BY-4.0
metadata:
  agent: conflict-referee
  agent-version: "1"
---

# Establish the facts

## What it does

Builds the record the decision will rest on. It matches the two deals to
one account or finds they are two customers, reads the rule at the
version published on the day the claim arrived, works out who was first
on the dated record and whether the partner brought the customer in, and
takes each side's account separately and in their own words.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Establish Who Was First**
  - `ref/prt/resolve-a-channel-conflict`, activity 6 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)
- **Hear Each Side Separately**
  - `ref/prt/resolve-a-channel-conflict`, activity 8 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)
- **Match the Two Records**
  - `ref/prt/resolve-a-channel-conflict`, activity 3 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)
- **Read the Rule as It Stood**
  - `ref/prt/resolve-a-channel-conflict`, activity 5 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)
- **Test Who Brought the Customer**
  - `ref/prt/resolve-a-channel-conflict`, activity 7 -
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
