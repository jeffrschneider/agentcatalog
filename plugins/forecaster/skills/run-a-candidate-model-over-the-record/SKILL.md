---
name: run-a-candidate-model-over-the-record
description: Runs a candidate model or profile over what already happened and reports how well it would have called it, and runs it beside what is in force today to show what would come out differently. Use it when running `ref/mkt/attribution-model` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Run a candidate model over the record

## What it does

Runs a candidate model or profile over what already happened and reports
how well it would have called it, and runs it beside what is in force
today to show what would come out differently.

## Where it happens

The agent does this in seven activities across four reference processes.
Each one names the activity as that process words it.

- **Back-Test the Candidates**
  - `ref/mkt/lead-scoring-model`, activity 9 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Check What Each Does to Routing**
  - `ref/mkt/lead-scoring-model`, activity 10 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Read How the Model Has Scored**
  - `ref/mkt/lead-scoring-model`, activity 2 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Recompute the Closed Periods**
  - `ref/mkt/attribution-model`, activity 9 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Run It Beside the Live Model**
  - `ref/mkt/lead-scoring-model`, activity 12 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Test the Candidates against the Record**
  - `ref/mkt/attribution-model`, activity 8 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
  - `ref/mkt/ideal-customer-profile`, activity 9 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Test the Persona against the Record**
  - `ref/mkt/buyer-persona`, activity 14 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
