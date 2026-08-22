---
name: run-a-controlled-test
description: Sets the terms of a test, which are the change, the audience it runs on and the measure that decides it. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: study-manager
  agent-version: "1"
---

# Run a controlled test

## What it does

Sets the terms of a test, which are the change, the audience it runs on
and the measure that decides it. It checks that nothing else is due on
the same visitors, starts the split once the owner says go, and watches
delivery and the guardrail measures while the test runs.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Clear the Traffic**
  - `ref/mkt/conversion-experiment`, activity 4 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Set the Terms of the Test**
  - `ref/mkt/conversion-experiment`, activity 2 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Start the Test**
  - `ref/mkt/conversion-experiment`, activity 11 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Watch the Test Run**
  - `ref/mkt/conversion-experiment`, activity 12 -
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
