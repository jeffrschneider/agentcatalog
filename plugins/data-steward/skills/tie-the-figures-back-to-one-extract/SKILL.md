---
name: tie-the-figures-back-to-one-extract
description: Pulls the open records at the cut-off, converts them to one currency, reconciles every cut against the extract they came from, and has a second person check it before anything goes out. Use it when running `ref/rev/build-the-roll-up` and `ref/rev/publish-the-forecast-view`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Tie the figures back to one extract

## What it does

Pulls the open records at the cut-off, converts them to one currency,
reconciles every cut against the extract they came from, and has a
second person check it before anything goes out. Every figure published
has to tie back to the roll-up.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Check Every Figure Ties to the Roll-Up**
  - `ref/rev/publish-the-forecast-view`, activity 9 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)
- **Convert to One Currency**
  - `ref/rev/build-the-roll-up`, activity 6 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Have a Second Pair of Eyes Check It**
  - `ref/rev/build-the-roll-up`, activity 15 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Pull the Open Deals at the Cut-Off**
  - `ref/rev/build-the-roll-up`, activity 4 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Reconcile the Cuts Against the Extract**
  - `ref/rev/build-the-roll-up`, activity 9 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)

## What to record

Per definition: the request and who made it, who reads the object today
and what counts off it, the sentence saying what the object is and what
it is not, every field with its fill rate and whether anything reads it,
the required list with the reason each field is required, the allowed
values with what each one means, the uniqueness key written as fields
rather than as a feeling, and where every field's value comes from. Then
the count of records already held that would fail, the reports and
integrations that read a changed field, the signed version with its
signer and date, and the backfill deadline with its owner and the count
still failing when the run closed. Per correction: the old value, the
new value and the reason, for every record touched. Per failure: the
source named with the evidence that it was that one, and a failure that
could not be traced recorded as unexplained rather than as fixed. Per
merge: the surviving id with the reason it was chosen, the winning value
per field naming the record it came from, and every value that did not
survive, stored against the survivor and dated.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
