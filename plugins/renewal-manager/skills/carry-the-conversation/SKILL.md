---
name: carry-the-conversation
description: Opens the conversation, keeps what the customer wants in their own words, settles what carries over and what is dropped or added, sends the offer, and reprices a term that comes back smaller against the floor rather than recording it as a loss. Use it when running `ref/sls/close-a-renewal`.
license: CC-BY-4.0
metadata:
  agent: renewal-manager
  agent-version: "1"
---

# Carry the conversation

## What it does

Opens the conversation, keeps what the customer wants in their own
words, settles what carries over and what is dropped or added, sends the
offer, and reprices a term that comes back smaller against the floor
rather than recording it as a loss.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Hear What the Customer Wants**
  - `ref/sls/close-a-renewal`, activity 3 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Open the Conversation**
  - `ref/sls/close-a-renewal`, activity 2 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Reprice a Smaller Term**
  - `ref/sls/close-a-renewal`, activity 10 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Send the Offer**
  - `ref/sls/close-a-renewal`, activity 8 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Settle What Carries Over**
  - `ref/sls/close-a-renewal`, activity 5 -
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
