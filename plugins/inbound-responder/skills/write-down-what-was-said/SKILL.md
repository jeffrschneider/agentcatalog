---
name: write-down-what-was-said
description: Writes the first conversation up against the record, including every commitment made in it, who made it and when it is due. Use it when running `ref/sls/answer-an-inbound-inquiry`.
license: CC-BY-4.0
metadata:
  agent: inbound-responder
  agent-version: "1"
---

# Write down what was said

## What it does

Writes the first conversation up against the record, including every
commitment made in it, who made it and when it is due.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Write Down What Was Said**
  - `ref/sls/answer-an-inbound-inquiry`, activity 12 -
    [Answer an Inbound Inquiry](../../../../processes/sales/answer-an-inbound-inquiry.md)

## What to record

Per inquiry: what was asked in the words it was asked in, the channel
and the arrival time, and the answer time that was promised. The
readings it answered from, each naming the system it came from and when
that reading was current, with any reading that could not be taken named
as unread rather than left out. The consent and do-not-contact check,
and the rule behind any no. The person named to answer. The reply at a
version, with the claim register entry behind every claim it makes. The
send time and channel. Every time offered and whether it was kept. Every
commitment made in the first conversation, with who made it and when it
is due. The answer time set against the promise, with a miss recorded as
a miss.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
