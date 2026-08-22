---
name: answer-from-the-library
description: Matches each question to an answer the library already holds at that answer's version, and reads every match back against the control, the policy or the report it came from. Use it when running `ref/sls/answer-a-security-questionnaire` and `ref/sls/respond-to-an-rfp`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Answer from the library

## What it does

Matches each question to an answer the library already holds at that
answer's version, and reads every match back against the control, the
policy or the report it came from. A match whose source no longer says
that is flagged rather than sent.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Answer the Requirements**
  - `ref/sls/respond-to-an-rfp`, activity 7 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Check the Matches Are Still True**
  - `ref/sls/answer-a-security-questionnaire`, activity 5 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Match Against the Library**
  - `ref/sls/answer-a-security-questionnaire`, activity 4 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)

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
