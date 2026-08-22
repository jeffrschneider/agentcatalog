---
name: send-it-and-answer-what-comes-back
description: Files the response, logs the date it landed, and gets a receipt from the buyer, because without one it is not in. Use it when running `ref/sls/answer-a-security-questionnaire` and `ref/sls/respond-to-an-rfp`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Send it and answer what comes back

## What it does

Files the response, logs the date it landed, and gets a receipt from the
buyer, because without one it is not in. Answers the follow-ups
afterwards and records how the whole thing ended.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Answer the Follow-Ups**
  - `ref/sls/answer-a-security-questionnaire`, activity 14 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Confirm Receipt**
  - `ref/sls/respond-to-an-rfp`, activity 15 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Record the Outcome**
  - `ref/sls/respond-to-an-rfp`, activity 17 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Send It and Log the Date**
  - `ref/sls/answer-a-security-questionnaire`, activity 13 -
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
