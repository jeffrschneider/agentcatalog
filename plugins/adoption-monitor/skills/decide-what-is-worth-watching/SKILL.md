---
name: decide-what-is-worth-watching
description: Picks with the process owner which steps matter enough to watch and which do not, and says in words a person can check what a followed step and a departed one look like in the data. Use it when running `ref/rev/instrument-a-process`.
license: CC-BY-4.0
metadata:
  agent: adoption-monitor
  agent-version: "1"
---

# Decide what is worth watching

## What it does

Picks with the process owner which steps matter enough to watch and
which do not, and says in words a person can check what a followed step
and a departed one look like in the data.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Pick the Steps Worth Watching**
  - `ref/rev/instrument-a-process`, activity 2 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)
- **Say What Departure Looks Like**
  - `ref/rev/instrument-a-process`, activity 3 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)

## What to record

Per process: the watched steps, and the unwatched ones with the reason
each was left out. For each watched step, the observable difference
between a followed run and a departed one. The change request field by
field, saying what each new field records about a person, and the policy
check with the line behind every refusal and the fields the privacy
reviewer struck out. The baseline, and the detection's score against the
known runs with every miss and every false alarm listed. Every signal
raised in the first weeks, checked by hand against the run it fired on.
The steps it still cannot see. Per period: the measure's gaps and
outages marked before a number is read, the ranked departures with the
count behind each rate, and what people said, attributed to a role, with
the refusals counted as refusals.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
