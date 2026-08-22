---
name: record-the-exploration
description: Files the run whether it proceeded or stopped, so the next run that names the same candidate can read what was already found. Use it when running `ref/prt/explore-an-alliance`.
license: CC-BY-4.0
metadata:
  agent: alliance-scout
  agent-version: "1"
---

# Record the exploration

## What it does

Files the run whether it proceeded or stopped, so the next run that
names the same candidate can read what was already found.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Record the Exploration**
  - `ref/prt/explore-an-alliance`, activity 16 -
    [Explore an Alliance](../../../../processes/partners/explore-an-alliance.md)

## What to record

The strategic reason as written before any company was named, dated. The
build, buy or ally comparison and what it concluded. The candidate list
with the source of each name. Per candidate: what they sell and to whom,
the fit score, the criteria it was scored on, and the inputs behind it.
The shortlist with the order of approach and who was to make it. Per
candidate approached: the date, the person who made contact, and the
mutual confidentiality agreement signed before anything beyond public
material was shown. The numbers each side traded and the agreement they
were traded under. The joint thesis at a version. The exploration
record, kept either way, readable by the next run that names the same
candidate.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
