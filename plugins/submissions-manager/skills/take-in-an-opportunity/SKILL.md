---
name: take-in-an-opportunity
description: The agent reads what an outside body is asking for, what it recognizes or covers, when it closes and what it costs, and records that against the body it came from. Use it when running `ref/mkt/award-entry`, `ref/mkt/brief-industry-analyst` and `ref/mkt/speaking-engagement`.
license: CC-BY-4.0
metadata:
  agent: submissions-manager
  agent-version: "1"
---

# Take in an opportunity

## What it does

The agent reads what an outside body is asking for, what it recognizes
or covers, when it closes and what it costs, and records that against
the body it came from.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Take in the Award**
  - `ref/mkt/award-entry`, activity 1 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
- **Take in the Call**
  - `ref/mkt/speaking-engagement`, activity 1 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)
- **Take in the Request**
  - `ref/mkt/brief-industry-analyst`, activity 1 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)

## What to record

The submissions record holds one entry for each body, with the
eligibility rules as they were read, the date they were read, the
deadline, and the format the body requires. Every filed entry is kept at
the version that was filed, with the date it went in and the sign-off it
went out under. Every question the judges or the analysts asked is
recorded with the answer given and the date it was given. The decision
is recorded when it arrives, together with what the body said about the
entry and whether the entry won.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
