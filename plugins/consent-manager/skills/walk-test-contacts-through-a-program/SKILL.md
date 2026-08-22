---
name: walk-test-contacts-through-a-program
description: Walks a test contact down every path a program can take and reports where the path does not do what the rules require. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Walk test contacts through a program

## What it does

Walks a test contact down every path a program can take and reports
where the path does not do what the rules require.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Run Test Contacts Through It**
  - `ref/mkt/nurture-sequence`, activity 12 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

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
