---
name: watch-the-responses-and-close-the-field
description: Tracks how many responses have come in against how many the study needs, half by half where the design has more than one half. Use it when running `ref/mkt/brand-health`, `ref/mkt/customer-research` and `ref/mkt/win-loss-analysis`.
license: CC-BY-4.0
metadata:
  agent: study-manager
  agent-version: "1"
---

# Watch the responses and close the field

## What it does

Tracks how many responses have come in against how many the study needs,
half by half where the design has more than one half. When the sample is
complete or the date arrives, it stops the asking and fixes the
responses.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Close the Interviews**
  - `ref/mkt/win-loss-analysis`, activity 14 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Close the Study**
  - `ref/mkt/customer-research`, activity 15 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Close the Wave**
  - `ref/mkt/brand-health`, activity 15 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
- **Watch Both Halves Fill**
  - `ref/mkt/win-loss-analysis`, activity 13 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Watch the Sample Fill**
  - `ref/mkt/brand-health`, activity 14 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 14 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)

## What to record

The study written down as a question before any data is gathered: what
it has to settle, the method chosen and why that method, who or what is
sampled, how many responses it needs, and the date the findings are due.
Every question and every piece of material at a version, in the order it
is put to people, with each response marked with the version it
answered. Every response as it was given, with its date, and every
response that was removed from the count, with the rule that removed it.
Each finding with the responses recorded under it, so the finding and
its evidence are read together. A comparison against the earlier studies
in the series, naming every place this study differs from the last one
and what that difference does to the reading. The count of responses
against the count the study planned for, said on the day the study
closes. The CONVENED and DONE records of everything it convenes.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
