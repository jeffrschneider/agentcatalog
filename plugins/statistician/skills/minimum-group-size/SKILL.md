---
name: minimum-group-size
description: Sets the group size below which no figure or comment is shown, so no answer or outcome can be traced to a person, sets the groups a survey or a report shows at or above it, and checks every table against it before anything goes out. Use it when running `ref/hr/report-on-the-workforce` and `ref/hr/run-the-employee-survey`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Minimum group size

## What it does

Sets the group size below which no figure or comment is shown, so no
answer or outcome can be traced to a person, sets the groups a survey or
a report shows at or above it, and checks every table against it before
anything goes out.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Report for Small Groups**
  - `ref/hr/report-on-the-workforce`, activity 12 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Set the Groups to Report**
  - `ref/hr/run-the-employee-survey`, activity 5 -
    [Run the Employee Survey](../../../../processes/human-resources/run-the-employee-survey.md)
- **Set the Minimum Group Size**
  - `ref/hr/run-the-employee-survey`, activity 4 -
    [Run the Employee Survey](../../../../processes/human-resources/run-the-employee-survey.md)

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
