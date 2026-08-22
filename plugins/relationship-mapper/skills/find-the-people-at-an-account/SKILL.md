---
name: find-the-people-at-an-account
description: Pulls the people the record already holds at an account and finds the ones it does not, inside the cap the run sets. Use it when running `ref/sls/map-the-account-people`.
license: CC-BY-4.0
metadata:
  agent: relationship-mapper
  agent-version: "1"
---

# Find the people at an account

## What it does

Pulls the people the record already holds at an account and finds the
ones it does not, inside the cap the run sets. Every person carries the
source they were found in and the date that source was published.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Find the People We Do Not Hold**
  - `ref/sls/map-the-account-people`, activity 4 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)
- **Pull the People We Already Hold**
  - `ref/sls/map-the-account-people`, activity 3 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)

## What to record

Per person: the decision they sit under, whether they decide, influence,
block or use, the source they were found in and that source's
publication date, the reporting line behind any claim of authority, the
strength score with the contact history it was computed from, the path
in and who at our end holds it, and the stance with what was said or
done behind it. Per map: every decision with no decider found or nobody
we know marked as a gap rather than left blank, what the privacy check
removed and the rule behind each removal, and the issued version naming
who corrected what and when they signed. A claim that somebody knows a
buyer well is recorded as a claim, with the person who made it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
