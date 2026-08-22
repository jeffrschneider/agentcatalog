---
name: say-what-moved-since-the-last-cycle
description: Sets this cycle against the last one on the same rules, works out what moved and why, and attaches that movement to the view when it is published. Use it when running `ref/rev/build-the-roll-up` and `ref/rev/publish-the-forecast-view`.
license: CC-BY-4.0
metadata:
  agent: roll-up-builder
  agent-version: "1"
---

# Say what moved since the last cycle

## What it does

Sets this cycle against the last one on the same rules, works out what
moved and why, and attaches that movement to the view when it is
published. Every definition, rate or cut-off change is marked at the
cycle it happened in.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Attach What Moved Since Last Time**
  - `ref/rev/publish-the-forecast-view`, activity 6 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)
- **Compute What Moved**
  - `ref/rev/build-the-roll-up`, activity 12 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Set It Against the Last Cycle**
  - `ref/rev/build-the-roll-up`, activity 10 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)

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
