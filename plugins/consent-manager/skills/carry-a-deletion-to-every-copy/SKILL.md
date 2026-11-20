---
name: carry-a-deletion-to-every-copy
description: For a person's data request, finds the consent record and every system that keeps its own copy of their contact details, with what each copy holds, and once the privacy lead has granted a deletion carries it to the owner of each system and confirms that each one took it, keeping only what stops the person being contacted again where the local rules allow. Use it when running `ref/sup/answer-a-data-request`.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Carry a deletion to every copy

## What it does

For a person's data request, finds the consent record and every system
that keeps its own copy of their contact details, with what each copy
holds, and once the privacy lead has granted a deletion carries it to
the owner of each system and confirms that each one took it, keeping
only what stops the person being contacted again where the local rules
allow.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Carry the Deletion to Every Copy**
  - `ref/sup/answer-a-data-request`, activity 12 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)
- **Find Every Copy of the Contact Details**
  - `ref/sup/answer-a-data-request`, activity 7 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)

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
