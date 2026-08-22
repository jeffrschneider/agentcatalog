---
name: close-the-ramp-out
description: Keeps the run open until the first customer conversation has been debriefed, naming what the customer asked that the joiner could not answer and the date each gap is fixed by, and reports where the joiner stands against the ramp plan. Use it when running `ref/rev/onboard-a-seller`.
license: CC-BY-4.0
metadata:
  agent: onboarding-manager
  agent-version: "1"
---

# Close the ramp out

## What it does

Keeps the run open until the first customer conversation has been
debriefed, naming what the customer asked that the joiner could not
answer and the date each gap is fixed by, and reports where the joiner
stands against the ramp plan.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Debrief the First Conversation**
  - `ref/rev/onboard-a-seller`, activity 16 -
    [Onboard a Seller](../../../../processes/revenue-operations/onboard-a-seller.md)
- **Report the Ramp**
  - `ref/rev/onboard-a-seller`, activity 17 -
    [Onboard a Seller](../../../../processes/revenue-operations/onboard-a-seller.md)

## What to record

Per joiner: the start as taken in, with the job, the manager and the
date. The job and the ramp in the manager's own words, from the briefing
that agreed them. Every access request with its system, the date it was
raised and the ticket it went under, and next to it the date the joiner
signed in successfully or the fact that they never did. The territory
and the ramped number at the version handed over. The learning plan at a
version, with the week each subject sits in, the person teaching it, and
a date against any change made after teaching started. Each session as
held or missed, and who covered a session the teacher missed. The calls
listened to, with dates. The sitting as scheduled, with what the joiner
was told they may bring. The first conversation as debriefed, naming
what the customer asked that the joiner could not answer and the date
each gap is fixed by. The ramp report at each checkpoint. An auditor can
read the run and see what was taught, what was open, and what the joiner
was never given.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
