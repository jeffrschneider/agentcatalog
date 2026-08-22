---
name: record-the-decision-and-pass-it-on
description: The agent chases the decision until it arrives, records it against the entry whether it won or lost, and passes a result worth announcing to whoever runs the announcement. Use it when running `ref/mkt/award-entry`.
license: CC-BY-4.0
metadata:
  agent: submissions-manager
  agent-version: "1"
---

# Record the decision and pass it on

## What it does

The agent chases the decision until it arrives, records it against the
entry whether it won or lost, and passes a result worth announcing to
whoever runs the announcement.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hand the Result On**
  - `ref/mkt/award-entry`, activity 15 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
- **Track the Result**
  - `ref/mkt/award-entry`, activity 14 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)

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
