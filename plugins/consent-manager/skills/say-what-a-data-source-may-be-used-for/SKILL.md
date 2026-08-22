---
name: say-what-a-data-source-may-be-used-for
description: "Reads the terms on each source of data and says what may be done with it: what may be read, whether touches may be joined to one person, what may be scored on, which traits may be used to target, and where the data is allowed to sit. Use it when running `ref/mkt/analyze-customer-base` and 4 other reference processes."
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Say what a data source may be used for

## What it does

Reads the terms on each source of data and says what may be done with
it: what may be read, whether touches may be joined to one person, what
may be scored on, which traits may be used to target, and where the data
is allowed to sit.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Check the Terms and the Data**
  - `ref/mkt/select-marketing-technology`, activity 11 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Clear the Data for This Use**
  - `ref/mkt/analyze-customer-base`, activity 4 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Clear the Data for Use**
  - `ref/mkt/attribution-model`, activity 6 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Clear the New Signals**
  - `ref/mkt/lead-scoring-model`, activity 6 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Clear the Targeting and the Data**
  - `ref/mkt/media-plan`, activity 4 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)

## What to record

For every list it clears, the count it removed and the rule each removal
was made under. For every withdrawal, a dated line naming each system
that keeps a copy of the audience, when the withdrawal was written into
it, and when the write was confirmed. A verdict per item for a scored
change, each citing the rule and its version. For every send it stopped,
the rule the send would have broken and the contacts it would have
reached.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
