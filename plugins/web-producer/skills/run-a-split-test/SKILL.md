---
name: run-a-split-test
description: Builds each version of a page and sets up how the traffic divides between them, confirms every version serves and its numbers arrive, starts the split when the owner says go, and afterwards puts one version in front of everyone or takes the change out. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Run a split test

## What it does

Builds each version of a page and sets up how the traffic divides
between them, confirms every version serves and its numbers arrive,
starts the split when the owner says go, and afterwards puts one version
in front of everyone or takes the change out.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Build the Variants**
  - `ref/mkt/conversion-experiment`, activity 7 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Carry out the Decision**
  - `ref/mkt/conversion-experiment`, activity 15 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Check the Setup**
  - `ref/mkt/conversion-experiment`, activity 10 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Start the Test**
  - `ref/mkt/conversion-experiment`, activity 11 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
