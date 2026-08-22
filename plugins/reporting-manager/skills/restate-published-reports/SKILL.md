---
name: restate-published-reports
description: Decides which already-published reports have to be restated after something underneath them changed and which of them still stand, then reissues each affected period as a new version. Use it when running `ref/mkt/attribution-model`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Restate published reports

## What it does

Decides which already-published reports have to be restated after
something underneath them changed and which of them still stand, then
reissues each affected period as a new version. The version it corrects
stays where it is.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Decide What Happens to Published Reports**
  - `ref/mkt/attribution-model`, activity 11 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Reissue the Affected Reports**
  - `ref/mkt/attribution-model`, activity 13 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
