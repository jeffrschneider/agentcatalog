---
name: size-the-work-and-the-shortfall
description: Works out how much work something takes and whether there is enough to carry it, which covers the hours one run costs, the load a new tool would take on, and where the demand passes what the department can do. Use it when running `ref/mkt/plan-marketing-capacity` and `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Size the work and the shortfall

## What it does

Works out how much work something takes and whether there is enough to
carry it, which covers the hours one run costs, the load a new tool
would take on, and where the demand passes what the department can do.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Find the Shortfall**
  - `ref/mkt/plan-marketing-capacity`, activity 6 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Size What the Tool Has to Carry**
  - `ref/mkt/select-marketing-technology`, activity 6 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Size the Effort Each Run Takes**
  - `ref/mkt/plan-marketing-capacity`, activity 5 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
