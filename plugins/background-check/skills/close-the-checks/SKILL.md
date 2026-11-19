---
name: close-the-checks
description: Hands the offer only the outcome, clear or decided, destroys the results and references when the retention period ends with a record that they were, and records how long each check took and what the disputes found. Use it when running `ref/hr/check-a-candidates-background`.
license: CC-BY-4.0
metadata:
  agent: background-check
  agent-version: "1"
---

# Close the checks

## What it does

Hands the offer only the outcome, clear or decided, destroys the results
and references when the retention period ends with a record that they
were, and records how long each check took and what the disputes found.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Destroy the Results on Time**
  - `ref/hr/check-a-candidates-background`, activity 16 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Hand the Outcome to the Offer**
  - `ref/hr/check-a-candidates-background`, activity 15 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Record What the Checks Taught**
  - `ref/hr/check-a-candidates-background`, activity 17 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)

## What to record

Each run leaves the checks the screening policy set for the role in each
location with the reason for each, the point the rules let each one run,
the notice the candidate received and their signed consent to each
check, each order with the details sent and the date, and each check
chased to its result. The results sit in the restricted store with a log
of every opening, and the hiring record holds only the outcome. Where a
check found something, the run leaves the copy the candidate received
and the date, the time allowed to respond, the candidate's explanation
or the error sent back and the corrected result, the named person's
decision with the reason in terms of the job, and the written notice of
that decision with the rights the rules require. Each run closes with
the outcome handed to the offer, the date the results and references
were destroyed with a record that they were, and how long each check
took. Nothing in the record shows this agent deciding on a finding.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
