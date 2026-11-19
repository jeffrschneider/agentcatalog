---
name: set-up-the-checks
description: Takes in the chosen candidate, confirms only the checks the screening policy sets for the role in each location and the point the rules let each one run, and gives the candidate a plain notice of each check with a request for written consent. Use it when running `ref/hr/check-a-candidates-background`.
license: CC-BY-4.0
metadata:
  agent: background-check
  agent-version: "1"
---

# Set up the checks

## What it does

Takes in the chosen candidate, confirms only the checks the screening
policy sets for the role in each location and the point the rules let
each one run, and gives the candidate a plain notice of each check with
a request for written consent.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Ask for Written Consent**
  - `ref/hr/check-a-candidates-background`, activity 4 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Confirm When the Checks May Run**
  - `ref/hr/check-a-candidates-background`, activity 3 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Confirm the Checks the Role Requires**
  - `ref/hr/check-a-candidates-background`, activity 2 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Take in the Chosen Candidate**
  - `ref/hr/check-a-candidates-background`, activity 1 -
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
