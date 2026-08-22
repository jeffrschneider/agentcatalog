---
name: measure-the-departments-throughput
description: Counts how much work the department got through, which is how many runs closed, how long each one took, and where they sat waiting. Use it when running `ref/mkt/plan-marketing-capacity`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Measure the departments throughput

## What it does

Counts how much work the department got through, which is how many runs
closed, how long each one took, and where they sat waiting.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Measure What the Department Got Through**
  - `ref/mkt/plan-marketing-capacity`, activity 4 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
