---
name: choose-the-method-and-draw-the-sample
description: Picks the method that will answer the question and says why that method rather than another, then decides who or what gets sampled, how the sample is drawn and how many responses it needs. Use it when running `ref/mkt/brand-health` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: study-manager
  agent-version: "1"
---

# Choose the method and draw the sample

## What it does

Picks the method that will answer the question and says why that method
rather than another, then decides who or what gets sampled, how the
sample is drawn and how many responses it needs. Where a run reads back
over existing records, it pulls the population those records describe
first.

## Where it happens

The agent does this in seven activities across six reference processes.
Each one names the activity as that process words it.

- **Choose the Method**
  - `ref/mkt/customer-research`, activity 3 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Define the Sample**
  - `ref/mkt/brand-health`, activity 7 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 6 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Design the Buyer Study**
  - `ref/mkt/map-buyer-journey`, activity 4 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Draw Both Samples**
  - `ref/mkt/win-loss-analysis`, activity 5 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Plan the Study**
  - `ref/mkt/buyer-persona`, activity 5 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
- **Pull the Closed Deals**
  - `ref/mkt/win-loss-analysis`, activity 2 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Size the Test**
  - `ref/mkt/conversion-experiment`, activity 3 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

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
