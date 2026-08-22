---
name: say-what-a-patch-can-carry
description: Models what each patch can carry against what it closed before, and reads that history again when the numbers are being set. Use it when running `ref/rev/model-the-territories` and `ref/rev/set-the-quotas`.
license: CC-BY-4.0
metadata:
  agent: territory-modeler
  agent-version: "1"
---

# Say what a patch can carry

## What it does

Models what each patch can carry against what it closed before, and
reads that history again when the numbers are being set. Beside every
carrying number sits the assumption it rests on and what would make that
assumption wrong. A number that cannot name its source is marked
unsourced where a reader sees it.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Model What Each Patch Carries**
  - `ref/rev/model-the-territories`, activity 8 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)
- **Read What Each Patch Carried**
  - `ref/rev/set-the-quotas`, activity 3 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)
- **Record What the Model Rests On**
  - `ref/rev/model-the-territories`, activity 14 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)

## What to record

Per run: the carve rule as it was agreed and the fields it reads, each
candidate map with every account placed exactly once, and a carrying
number per patch naming the data it was computed from. A number that
cannot name its source is marked unsourced where a reader sees it. The
maps that lost are kept, each with the reason it lost. The fixed map
carries its version, the rule it was drawn on and the date it takes
effect, and beside every carrying number sits the assumption it rests on
and what would make that assumption wrong. Anybody auditing a run can
redraw it from what is written down.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
