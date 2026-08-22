---
name: record-what-was-learned
description: The agent writes down what to repeat and what to avoid next cycle, and keeps it against the body, so the next submission starts from what the last one taught. Use it when running `ref/mkt/award-entry`, `ref/mkt/brief-industry-analyst` and `ref/mkt/speaking-engagement`.
license: CC-BY-4.0
metadata:
  agent: submissions-manager
  agent-version: "1"
---

# Record what was learned

## What it does

The agent writes down what to repeat and what to avoid next cycle, and
keeps it against the body, so the next submission starts from what the
last one taught.

## Where it happens

The agent does this in one activity across three reference processes.
Each one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/mkt/award-entry`, activity 16 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
  - `ref/mkt/brief-industry-analyst`, activity 17 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
  - `ref/mkt/speaking-engagement`, activity 16 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)

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
