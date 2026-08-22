---
name: take-in-what-the-study-must-settle
description: Reads the request that started the study and works out what it has to settle and by when. Use it when running `ref/mkt/brand-audit` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: study-manager
  agent-version: "1"
---

# Take in what the study must settle

## What it does

Reads the request that started the study and works out what it has to
settle and by when. That covers the question a piece of research must
answer, the period a review reads back over, and what a proposed change
is meant to do and to whom.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Take in the Hypothesis**
  - `ref/mkt/conversion-experiment`, activity 1 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Take in the Period**
  - `ref/mkt/win-loss-analysis`, activity 1 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Take in the Question**
  - `ref/mkt/customer-research`, activity 1 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Take in the Request**
  - `ref/mkt/brand-audit`, activity 1 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)

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
