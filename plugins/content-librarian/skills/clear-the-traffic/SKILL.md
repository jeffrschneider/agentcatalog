---
name: clear-the-traffic
description: Other tests and changes due on the same visitors. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Clear the Traffic

## What happens

Other tests and changes due on the same visitors.

## Where it happens

- `ref/mkt/conversion-experiment`, activity 4 -
  [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

## What to record

The inventory at a version every time it is rebuilt, with each live page
carrying what it was made to do, the date it last changed, what it is
doing now, and where every figure came from. The refresh cycle's list,
giving the reason each page is on it, and a line for the pages that were
looked at and left for a later cycle. A decision record for every merge,
retirement and redirect, naming the version that came down, what now
stands at its address, and the person who said so. A page it could not
measure is recorded as unmeasured, with the reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
