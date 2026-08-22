---
name: pull-the-numbers-from-the-systems
description: Reads the organization's own records to answer a question about accounts, channels or signals. Use it when running `ref/mkt/account-based-play`, `ref/mkt/lead-scoring-model` and `ref/mkt/media-plan`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Pull the numbers from the systems

## What it does

Reads the organization's own records to answer a question about
accounts, channels or signals. It comes back with what each account or
channel has actually done, and names the system and the date every
figure came from.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Gather the Candidate Signals**
  - `ref/mkt/lead-scoring-model`, activity 5 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Gather the Channel Evidence**
  - `ref/mkt/media-plan`, activity 5 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Read the Accounts**
  - `ref/mkt/account-based-play`, activity 2 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
