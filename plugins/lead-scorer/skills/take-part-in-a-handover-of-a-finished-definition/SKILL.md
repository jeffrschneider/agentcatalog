---
name: take-part-in-a-handover-of-a-finished-definition
description: Takes part in the handover of a finished definition, such as a profile, a persona, a set of segments, a scoring model or a set of findings, and says what changes about how leads are scored and routed as a result. Use it when running `ref/mkt/analyze-customer-base` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Take part in a handover of a finished definition

## What it does

Takes part in the handover of a finished definition, such as a profile,
a persona, a set of segments, a scoring model or a set of findings, and
says what changes about how leads are scored and routed as a result.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Hand over the Findings**
  - `ref/mkt/analyze-customer-base`, activity 17 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Hand over the Model**
  - `ref/mkt/lead-scoring-model`, activity 14 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Hand over the Persona**
  - `ref/mkt/buyer-persona`, activity 18 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
- **Hand over the Profile**
  - `ref/mkt/ideal-customer-profile`, activity 15 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Hand over the Segments**
  - `ref/mkt/segment-the-market`, activity 16 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
