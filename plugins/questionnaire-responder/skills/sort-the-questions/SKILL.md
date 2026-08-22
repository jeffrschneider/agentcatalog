---
name: sort-the-questions
description: Sorts the questions into areas and absorbs the ones that ask the same thing twice, then puts one owner and one date on every requirement that has to come back answered. Use it when running `ref/sls/answer-a-security-questionnaire` and `ref/sls/respond-to-an-rfp`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Sort the questions

## What it does

Sorts the questions into areas and absorbs the ones that ask the same
thing twice, then puts one owner and one date on every requirement that
has to come back answered.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Sort the Questions**
  - `ref/sls/answer-a-security-questionnaire`, activity 3 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Split the Requirements**
  - `ref/sls/respond-to-an-rfp`, activity 5 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)

## What to record

Per response: the rules the form set, written down before any answer was
drafted. Every question with the area it was sorted into and the
duplicates it absorbed. Every match with the answer version, the source
behind it and how close the match actually is. Every match the check
found no longer true, with the source that contradicts it. Every
question routed as unanswerable, with the person it went to and the date
it was needed. The approved answers at the version signed, the form as
filled with each attachment at its version, the check result with the
question or the rule behind every failure, and the date the response was
ready next to the date it landed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
