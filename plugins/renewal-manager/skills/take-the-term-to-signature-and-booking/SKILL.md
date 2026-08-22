---
name: take-the-term-to-signature-and-booking
description: Settles the words of the next term, takes it to signature, and books what the signed agreement says line for line against it. Use it when running `ref/sls/close-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: renewal-manager
  agent-version: "1"
---

# Take the term to signature and booking

## What it does

Settles the words of the next term, takes it to signature, and books
what the signed agreement says line for line against it. Nothing is
booked that the signature does not carry.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Agree the Words**
  - `ref/sls/close-a-renewal`, activity 11 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Book the Renewal**
  - `ref/sls/close-a-renewal`, activity 13 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Get the Signature**
  - `ref/sls/close-a-renewal`, activity 12 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)

## What to record

Per renewal: the clock, opened from the agreement's own dates, with the
date the position is due. The agreement as read, with a settled reading
attached to any clause that could be read two ways. The entitlements at
their signed level with the amendments. The commitments made at
signature and still open, each with who owes it and since when. The
shape of the next term and the reason for it. The ask and the floor at
the version a person approved, with that person named. The brief at a
version, with the usage and the standing attached rather than
summarized. The customer's own words, kept rather than replaced by a
summary. What carries over, what is dropped, what is added. A smaller
term recorded beside the old price with its distance from the floor
stated. The signed agreement, and the booked term set against it line
for line. Why the term grew, held or shrank, in a form the next renewal
can read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
