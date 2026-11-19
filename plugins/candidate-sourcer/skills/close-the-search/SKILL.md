---
name: close-the-search
description: Brings each person who said yes into the pipeline with their source, records every answer with the date each person may be approached again, removes the details of everyone else on time, and records which sources found people who went forward. Use it when running `ref/hr/find-candidates`.
license: CC-BY-4.0
metadata:
  agent: candidate-sourcer
  agent-version: "1"
---

# Close the search

## What it does

Brings each person who said yes into the pipeline with their source,
records every answer with the date each person may be approached again,
removes the details of everyone else on time, and records which sources
found people who went forward.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Bring the Interested People In**
  - `ref/hr/find-candidates`, activity 15 -
    [Find Candidates](../../../../processes/human-resources/find-candidates.md)
- **Record What the Search Taught**
  - `ref/hr/find-candidates`, activity 18 -
    [Find Candidates](../../../../processes/human-resources/find-candidates.md)
- **Record the Answers**
  - `ref/hr/find-candidates`, activity 16 -
    [Find Candidates](../../../../processes/human-resources/find-candidates.md)
- **Remove the Data No Longer Needed**
  - `ref/hr/find-candidates`, activity 17 -
    [Find Candidates](../../../../processes/human-resources/find-candidates.md)

## What to record

Each search leaves the hiring plan at the version it searched for, the
request for referrals and the teams it went to, each referral with the
employee who made it, how they know the person and the person's
agreement to be contacted, and each person found recorded once with the
first source that found them and the date. Each person carries the
reading against the must-haves with the evidence found for each and what
is still unclear, and the check of who may be approached with the reason
anyone was left out. Each approach is kept as drafted with where the
person's details came from, beside the recruiter's choice and the date
it was sent, with at most one follow-up. The search closes with each
person who said yes added as a candidate with their source, who said no
or did not reply and when each may be approached again, a record that
the details of the rest were removed and when, and how many each source
found and sent forward. Nothing in the record shows this agent sending
an approach or giving a referral weight in the screen.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
