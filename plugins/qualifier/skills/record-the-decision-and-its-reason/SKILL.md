---
name: record-the-decision-and-its-reason
description: Carries the decision onto the record with who made it, the date, the reason and the evidence under it, and records what the run taught about the questions that were asked. Use it when running `ref/sls/qualify-an-opportunity`.
license: CC-BY-4.0
metadata:
  agent: qualifier
  agent-version: "1"
---

# Record the decision and its reason

## What it does

Carries the decision onto the record with who made it, the date, the
reason and the evidence under it, and records what the run taught about
the questions that were asked.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/sls/qualify-an-opportunity`, activity 16 -
    [Qualify an Opportunity](../../../../processes/sales/qualify-an-opportunity.md)
- **Record the Decision and Its Reason**
  - `ref/sls/qualify-an-opportunity`, activity 15 -
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
