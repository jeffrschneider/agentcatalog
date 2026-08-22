---
name: set-the-answers-against-the-profile
description: Sets what came back against the customer profile, line by line and against a named version of it. Use it when running `ref/sls/qualify-an-opportunity`.
license: CC-BY-4.0
metadata:
  agent: qualifier
  agent-version: "1"
---

# Set the answers against the profile

## What it does

Sets what came back against the customer profile, line by line and
against a named version of it. Lists every question that came back empty
instead of filling it in with an assumption.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Fit Against the Profile**
  - `ref/sls/qualify-an-opportunity`, activity 10 -
    [Qualify an Opportunity](../../../../processes/sales/qualify-an-opportunity.md)
- **Record the Gaps**
  - `ref/sls/qualify-an-opportunity`, activity 12 -
    [Qualify an Opportunity](../../../../processes/sales/qualify-an-opportunity.md)

## What to record

The questions as written before they were asked, naming the version of
the question set they came from. Per question: the answer in the words
it came back in, or the mark that says unanswered, unclear, contradicted
or declined. Nothing is filled in with an assumption. The fit check line
by line against the profile version. The gaps, listed. The decision, who
made it, the date, the reason, and the evidence under it. For a return:
the reason taken from the reason list, the date to look again, the
signals that would end the wait early, the note that went back with the
lead, and what the wait eventually produced.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
