---
name: collect-the-sign-offs
description: Puts a finished piece in front of the people who have to approve it before it goes outside and records each answer against the piece. Use it when running `ref/mkt/enable-channel-partner`.
license: CC-BY-4.0
metadata:
  agent: rights-register
  agent-version: "1"
---

# Collect the sign offs

## What it does

Puts a finished piece in front of the people who have to approve it
before it goes outside and records each answer against the piece.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Get Sign-Offs**
  - `ref/mkt/enable-channel-partner`, activity 8 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)

## What to record

The rights record, with one entry per source saying what the source is,
who granted it, what the license covers, the channels and territories it
may run on, the date it starts, the date it ends, and where the document
is kept. A verdict for every source put to it before production, naming
the source, the channels and territories it was checked against, the
answer, and the term the answer rests on. For every finished asset, the
list of sources it rests on, each tied to the rights record entry that
cleared it and the version of the asset that used it. A dated warning
for every license running out, naming the published work that rests on
it and the date the license ends. A source whose rights it could not
establish is recorded as uncleared, with what is missing, rather than
being left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
