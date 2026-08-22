---
name: test-a-claim-against-its-evidence
description: The agent checks whether the evidence under a statement carries what the statement claims, and names the gap where it does not. Use it when running `ref/mkt/brand-positioning` and `ref/mkt/product-positioning`.
license: CC-BY-4.0
metadata:
  agent: editor
  agent-version: "1"
---

# Test a claim against its evidence

## What it does

The agent checks whether the evidence under a statement carries what the
statement claims, and names the gap where it does not.

## Where it happens

The agent does this in one activity across two reference processes. Each
one names the activity as that process words it.

- **Test the Positions against the Evidence**
  - `ref/mkt/brand-positioning`, activity 7 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
  - `ref/mkt/product-positioning`, activity 9 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)

## What to record

Every edit at a version, saying what has to change and why, item by
item, in terms the writer can work through without coming back to ask
what was meant. A line for anything it flagged for another pass, naming
the agent it went to. When it holds the version, the merge, the decline
or the revision request it gave in every round, each with its reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
