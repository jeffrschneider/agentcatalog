---
name: keep-the-pipeline
description: Logs each application and internal application with its source, acknowledges it, withholds the details the screen does not need, releases them only for those going forward and only to the people who book their interviews, hands candidates from the screen to the interviews and on to the checks and the offer, keeps on file only those who agreed, and passes an accepted move to the record. Use it when running `ref/hr/move-an-employee-to-a-new-role`, `ref/hr/run-the-interviews` and `ref/hr/screen-applications`.
license: CC-BY-4.0
metadata:
  agent: recruiting-coordinator
  agent-version: "1"
---

# Keep the pipeline

## What it does

Logs each application and internal application with its source,
acknowledges it, withholds the details the screen does not need,
releases them only for those going forward and only to the people who
book their interviews, hands candidates from the screen to the
interviews and on to the checks and the offer, keeps on file only those
who agreed, and passes an accepted move to the record.

## Where it happens

The agent does this in ten activities across three reference processes.
Each one names the activity as that process words it.

- **Acknowledge the Application**
  - `ref/hr/screen-applications`, activity 2 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Hand the Candidates to the Interviews**
  - `ref/hr/screen-applications`, activity 11 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Hand the Chosen Candidate On**
  - `ref/hr/run-the-interviews`, activity 18 -
    [Run the Interviews](../../../../processes/human-resources/run-the-interviews.md)
- **Keep Applicants on File by Consent**
  - `ref/hr/screen-applications`, activity 14 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Pass the Move to the Record**
  - `ref/hr/move-an-employee-to-a-new-role`, activity 15 -
    [Move an Employee to a New Role](../../../../processes/human-resources/move-an-employee-to-a-new-role.md)
- **Release the Details to Those Who Need Them**
  - `ref/hr/screen-applications`, activity 10 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Take In Internal Applications**
  - `ref/hr/move-an-employee-to-a-new-role`, activity 4 -
    [Move an Employee to a New Role](../../../../processes/human-resources/move-an-employee-to-a-new-role.md)
- **Take in Each Application**
  - `ref/hr/screen-applications`, activity 1 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)
- **Take in the Candidates**
  - `ref/hr/run-the-interviews`, activity 1 -
    [Run the Interviews](../../../../processes/human-resources/run-the-interviews.md)
- **Withhold What the Step Does Not Need**
  - `ref/hr/screen-applications`, activity 3 -
    [Screen Applications](../../../../processes/human-resources/screen-applications.md)

## What to record

A hiring plan leaves the approved position it came from, the must-haves
at each draft with every flag the check raised and how it was settled,
the interview plan with each question tied to one must-have, the scoring
scale, the panel and each interviewer's training, the sources and the
dates, signed by the hiring manager and the recruiter at a version. A
posting leaves each place it ran, every requirement read against the
must-haves, every wording flag with the word and the reason, each
approved version with the date it went live and the date it came down,
the test application from each channel, and how many applied from each
place and met every must-have. A screen leaves each application with its
source and the date, the acknowledgment, the list of details withheld,
each note as checked with any point struck and why, the details released
and to whom, the recruiter's decision on each applicant, the answer sent
and its date, and who agreed to be kept on file. A loop leaves each
interviewer's pack, every scorecard with the time it was submitted,
every remark struck with the reason, the debrief pack, the hiring
manager's decision with its reasons and the scores it rests on, the
reserves in order, and the date each candidate heard back. An internal
move leaves the same plan and loop, each internal applicant's answer and
reasons, the written offer as the hiring manager made it, and the move
passed to the record. Nothing in the record shows this agent deciding
about a candidate.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
