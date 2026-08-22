---
name: take-the-form-in-and-read-its-rules
description: "Takes in the form or the request with the buyer it came from, and reads the rules it sets before any answer is drafted: the deadline, the format, the channel, the limits and the window for questions. Use it when running `ref/sls/answer-a-security-questionnaire` and `ref/sls/respond-to-an-rfp`."
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Take the form in and read its rules

## What it does

Takes in the form or the request with the buyer it came from, and reads
the rules it sets before any answer is drafted: the deadline, the
format, the channel, the limits and the window for questions. That
window is used to ask the buyer what the document does not make clear,
while it is still open.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Ask the Buyer's Questions**
  - `ref/sls/respond-to-an-rfp`, activity 6 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Read the Rules It Sets**
  - `ref/sls/answer-a-security-questionnaire`, activity 2 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
  - `ref/sls/respond-to-an-rfp`, activity 2 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Take in the Questionnaire**
  - `ref/sls/answer-a-security-questionnaire`, activity 1 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Take in the Request**
  - `ref/sls/respond-to-an-rfp`, activity 1 -
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
