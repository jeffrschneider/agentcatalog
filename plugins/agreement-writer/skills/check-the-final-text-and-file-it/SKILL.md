---
name: check-the-final-text-and-file-it
description: Reads the final text against the agreed list, term by term, then files the executed copy and writes the terms other processes rely on back where they can be read. Use it when running `ref/prt/sign-a-partner-agreement`.
license: CC-BY-4.0
metadata:
  agent: agreement-writer
  agent-version: "1"
---

# Check the final text and file it

## What it does

Reads the final text against the agreed list, term by term, then files
the executed copy and writes the terms other processes rely on back
where they can be read.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Paper Against the Agreement**
  - `ref/prt/sign-a-partner-agreement`, activity 14 -
    [Sign a Partner Agreement](../../../../processes/partners/sign-a-partner-agreement.md)
- **Record It and Hand It On**
  - `ref/prt/sign-a-partner-agreement`, activity 17 -
    [Sign a Partner Agreement](../../../../processes/partners/sign-a-partner-agreement.md)

## What to record

Every draft at a version, with what changed from the version before it.
The numbered change list, each change marked give, trade or refuse, with
the reason and the internal approval that cleared it. The departures
from the standard terms listed apart from the standard terms, so a
reader can see in one place what this partner got that others did not.
Each qualification condition traced to the term that carries it, or to
the person who decided to drop it. The final read of the text against
the agreed list, term by term. The executed copy with its date and the
people it went to.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
