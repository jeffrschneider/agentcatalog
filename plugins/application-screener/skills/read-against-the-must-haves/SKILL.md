---
name: read-against-the-must-haves
description: Reads each application, with the details the step does not need withheld, against the written must-haves at the plan's version and nothing else, and writes a short note in which every point cites its must-have, what the application shows for it and what it leaves unclear. Use it when running `ref/hr/screen-applications`.
license: CC-BY-4.0
metadata:
  agent: application-screener
  agent-version: "1"
---

# Read against the must haves

## What it does

Reads each application, with the details the step does not need
withheld, against the written must-haves at the plan's version and
nothing else, and writes a short note in which every point cites its
must-have, what the application shows for it and what it leaves unclear.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Read Against the Must-Haves**
  - `ref/hr/screen-applications`, activity 4 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Write the Screening Note**
  - `ref/hr/screen-applications`, activity 5 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)

## What to record

Each application read leaves its note at a version, with the hiring plan
version it was read against, each point citing its must-have, what the
application shows for it and what it leaves unclear. Each flag leaves
the application it concerns and the reason it could not be read fairly.
Each note the recruiting-coordinator agent struck or sent back is kept
with the reason and the note written in its place. Nothing in the record
shows this agent ranking, turning down or choosing an applicant, and
nothing in a note refers to a withheld detail or a protected
characteristic.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
