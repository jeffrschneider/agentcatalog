---
name: set-the-rules-that-take-a-contact-out
description: Writes the rules that end a contact's run through a program and says where that contact goes next. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Set the rules that take a contact out

## What it does

Writes the rules that end a contact's run through a program and says
where that contact goes next.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Set the Exits**
  - `ref/mkt/nurture-sequence`, activity 5 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
