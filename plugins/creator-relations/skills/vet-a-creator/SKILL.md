---
name: vet-a-creator
description: Checks a named creator before anybody is offered money. Use it when running `ref/mkt/influencer-campaign`.
license: CC-BY-4.0
metadata:
  agent: creator-relations
  agent-version: "1"
---

# Vet a creator

## What it does

Checks a named creator before anybody is offered money. It reads the
audience figures against the measurement sources to see whether the
reach is real, reads what the creator has already published, and records
what each check found and the date it was run.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Vet the Candidates**
  - `ref/mkt/influencer-campaign`, activity 5 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)

## What to record

For each creator, the record holds the audience figures with the date
they were read and the source they came from, what the authenticity
check found, and what the history check found in the creator's past
publishing. For each deal, it keeps what was agreed at the version it
was agreed: every deliverable, the date each one is due, the channels
the work may run on, how long the organization may use it, what the
disclosure has to say, and the fee. Every approach lands with its date,
what was offered, and the answer that came back, including the creators
who declined and the reason they gave. When a creator publishes, the
agent records what went out, where it went out, and on what date. When a
check finds a problem, the agent records the finding, what it asked the
creator to do, the date it asked, and what the creator did.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
