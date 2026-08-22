---
name: test-the-stages-against-the-record
description: Whether each signal can be read, and who moved that way. Use it when running `ref/mkt/map-buyer-journey`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Test the Stages against the Record

## What happens

Whether each signal can be read, and who moved that way.

## Where it happens

- `ref/mkt/map-buyer-journey`, activity 11 -
  [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)

## What to record

Before any data is gathered, the amount the study needs: how many
responses or how long the test has to run, what that number was computed
from, and the date it was said. Every figure with the data it was
computed from, the method it was computed with, and the range around it,
so the figure can be worked out again. Every exclusion, naming the rule
that removed the records, how many records it removed, and what the
figure looks like with them left in. Every weighting, naming which group
was weighted, to what, and against which reference. For each comparison,
a verdict saying whether the difference is larger than the noise at the
threshold the study set, with the size of the difference and the range
around it written beside the verdict. A list of every figure it could
not compute with the data it had, marked as such and carried into the
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
