---
name: run-the-checks
description: Orders each consented check from the provider with only the details it needs, chases each one to a result by its date, and holds the results apart where only the named people can open them, with every opening logged. Use it when running `ref/hr/check-a-candidates-background`.
license: CC-BY-4.0
metadata:
  agent: background-check
  agent-version: "1"
---

# Run the checks

## What it does

Orders each consented check from the provider with only the details it
needs, chases each one to a result by its date, and holds the results
apart where only the named people can open them, with every opening
logged.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Hold the Results Apart**
  - `ref/hr/check-a-candidates-background`, activity 10 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Order the Checks**
  - `ref/hr/check-a-candidates-background`, activity 8 -
    [Check a Candidate's Background](../../../../processes/human-resources/check-a-candidates-background.md)
- **Track the Checks**
  - `ref/hr/check-a-candidates-background`, activity 9 -
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
