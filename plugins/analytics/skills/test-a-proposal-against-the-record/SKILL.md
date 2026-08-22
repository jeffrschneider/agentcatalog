---
name: test-a-proposal-against-the-record
description: The agent runs a proposed profile, persona, stage map, scoring rule or theme over what has already happened, and says whether it would have picked the outcomes the record shows. Use it when running `ref/mkt/buyer-persona` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Test a proposal against the record

## What it does

The agent runs a proposed profile, persona, stage map, scoring rule or
theme over what has already happened, and says whether it would have
picked the outcomes the record shows. It names where the proposal and
the record disagree.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Back-Test the Candidates**
  - `ref/mkt/lead-scoring-model`, activity 9 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Set the Themes against the Record**
  - `ref/mkt/win-loss-analysis`, activity 17 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Test the Candidates against the Record**
  - `ref/mkt/ideal-customer-profile`, activity 9 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Test the Persona against the Record**
  - `ref/mkt/buyer-persona`, activity 14 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
- **Test the Stages against the Record**
  - `ref/mkt/map-buyer-journey`, activity 11 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
