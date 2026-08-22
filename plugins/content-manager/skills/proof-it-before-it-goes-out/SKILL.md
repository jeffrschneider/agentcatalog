---
name: proof-it-before-it-goes-out
description: Reads test copies the way a reader will get them and finds what is wrong while it can still be fixed. Use it when running `ref/mkt/customer-newsletter`.
license: CC-BY-4.0
metadata:
  agent: content-manager
  agent-version: "1"
---

# Proof it before it goes out

## What it does

Reads test copies the way a reader will get them and finds what is wrong
while it can still be fixed.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Proof the Issue**
  - `ref/mkt/customer-newsletter`, activity 11 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)

## What to record

The request as it was accepted, with the date the piece promised and
what the piece is meant to accomplish. The CONVENED and DONE records of
everything it convenes. The publish record, naming who said go and which
version went live. The performance readout at the cadence the process
sets, and the decision it made after reading that readout: leave the
piece alone, update it, or retire it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
