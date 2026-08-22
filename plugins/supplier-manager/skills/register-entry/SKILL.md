---
name: register-entry
description: Lands a new agreement in the register with everything a later reader needs, which is what it is for, what it costs, the term, the renewal date and the named owner, and hands it to that owner with a date to review it. Use it when running `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: supplier-manager
  agent-version: "1"
---

# Register entry

## What it does

Lands a new agreement in the register with everything a later reader
needs, which is what it is for, what it costs, the term, the renewal
date and the named owner, and hands it to that owner with a date to
review it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hand It to the Owner**
  - `ref/mkt/select-marketing-technology`, activity 20 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Write It into the Register**
  - `ref/mkt/select-marketing-technology`, activity 19 -
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
