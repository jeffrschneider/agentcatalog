---
name: take-in-an-answered-inquiry
description: Takes the answered inquiry in with everything read on the way to it, so the questions that follow are asked against what is already known rather than from a blank page. Use it when running `ref/sls/answer-an-inbound-inquiry` and `ref/sls/qualify-an-opportunity`.
license: CC-BY-4.0
metadata:
  agent: qualifier
  agent-version: "1"
---

# Take in an answered inquiry

## What it does

Takes the answered inquiry in with everything read on the way to it, so
the questions that follow are asked against what is already known rather
than from a blank page.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand It to Qualification**
  - `ref/sls/answer-an-inbound-inquiry`, activity 13 -
    [Answer an Inbound Inquiry](../../../../processes/sales/answer-an-inbound-inquiry.md)
- **Take in the Answered Inquiry**
  - `ref/sls/qualify-an-opportunity`, activity 1 -
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
