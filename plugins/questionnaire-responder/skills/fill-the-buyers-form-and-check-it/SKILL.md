---
name: fill-the-buyers-form-and-check-it
description: Fills the buyer's own format word for word and attaches the evidence at the versions the answers name. Use it when running `ref/sls/answer-a-security-questionnaire` and `ref/sls/respond-to-an-rfp`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Fill the buyers form and check it

## What it does

Fills the buyer's own format word for word and attaches the evidence at
the versions the answers name. Checks the whole thing before it leaves:
every question answered, every limit obeyed, with the question or the
rule behind each failure named.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Attach the Evidence**
  - `ref/sls/answer-a-security-questionnaire`, activity 11 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Check It Against the Rules**
  - `ref/sls/respond-to-an-rfp`, activity 12 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Check the Form Before It Leaves**
  - `ref/sls/answer-a-security-questionnaire`, activity 12 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Fill the Buyer's Form**
  - `ref/sls/answer-a-security-questionnaire`, activity 10 -
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
