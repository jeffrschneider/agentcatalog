---
name: check-a-published-figure-ties-to-its-version
description: Carries the frozen version into the published view and checks that every figure on it rebuilds from the roll-up it claims to come from. Use it when running `ref/rev/publish-the-forecast-view`.
license: CC-BY-4.0
metadata:
  agent: roll-up-builder
  agent-version: "1"
---

# Check a published figure ties to its version

## What it does

Carries the frozen version into the published view and checks that every
figure on it rebuilds from the roll-up it claims to come from.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check Every Figure Ties to the Roll-Up**
  - `ref/rev/publish-the-forecast-view`, activity 9 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)
- **Take in the Frozen Roll-Up**
  - `ref/rev/publish-the-forecast-view`, activity 1 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)

## What to record

The cut-off with its time zone, and the cut-off the last cycle used. The
extract with its row count and its total. Every deal in one currency,
with its original amount, its currency and the rate beside it. Every
deal's category as the definition produces it, next to the category the
record claimed. Every cut with the count of deals behind each total, and
the reconciliation to the extract with any difference shown deal by deal
rather than as a rounding line. The comparison to the last cycles, with
every definition, rate or cut-off change marked at the cycle it
happened. The questions this roll-up could not answer, each with the
reason. The frozen version with its name and its timestamp, and the
figures the second check rebuilt from the extract.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
