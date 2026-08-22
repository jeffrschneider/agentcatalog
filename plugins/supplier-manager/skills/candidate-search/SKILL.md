---
name: candidate-search
description: Finds every candidate worth looking at against the requirements, then narrows the list by dropping the ones that miss a requirement, so what is left can be looked at properly. Use it when running `ref/mkt/engage-marketing-agency` and `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: supplier-manager
  agent-version: "1"
---

# Candidate search

## What it does

Finds every candidate worth looking at against the requirements, then
narrows the list by dropping the ones that miss a requirement, so what
is left can be looked at properly.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Candidate List**
  - `ref/mkt/engage-marketing-agency`, activity 7 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Cut to a Shortlist**
  - `ref/mkt/select-marketing-technology`, activity 9 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Search the Market**
  - `ref/mkt/select-marketing-technology`, activity 8 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

## What to record

The register holds one entry for each supplier, subscription, agreement,
membership and registration: what it is for, the agent or the person who
owns it, what it costs, the term, the renewal date, and the notice a
cancellation needs. An entry missing an owner or a renewal date is
recorded as missing them rather than left out of the register. For every
search, the requirements and the criteria at a version with the date
they were written, the candidates that were looked at and where each one
came from, the candidates dropped before scoring with the requirement
each one failed, and what the search itself cost to run. Every answer a
candidate gave, attributed to the candidate and dated. A dated notice
for each renewal, naming who was told, when they were told, and what the
owner decided. For every entry that ended, the date it ended, who
decided to end it, and what happened to the material or the data the
outside party was holding. For every registration, what was registered,
with which body, on what date, and when it has to be renewed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
