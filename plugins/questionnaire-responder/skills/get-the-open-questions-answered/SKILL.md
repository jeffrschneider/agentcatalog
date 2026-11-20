---
name: get-the-open-questions-answered
description: Routes every question the source cannot answer to the person who owns that fact, in the requester's own wording, and drafts what comes back into an answer named people sign. Use it when running `ref/fin/respond-to-a-tax-audit` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Get the open questions answered

## What it does

Routes every question the source cannot answer to the person who owns
that fact, in the requester's own wording, and drafts what comes back
into an answer named people sign. The security and legal parts are
answered the same way, from a maintained source rather than from memory.

## Where it happens

The agent does this in five activities across six reference processes.
Each one names the activity as that process words it.

- **Answer the Security and Legal Parts**
  - `ref/sls/respond-to-an-rfp`, activity 10 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Draft the New Answers**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 8 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)
  - `ref/sls/answer-a-security-questionnaire`, activity 7 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Route What Is Not Answered**
  - `ref/sls/answer-a-security-questionnaire`, activity 6 -
    [Answer a Security Questionnaire](../../../../processes/sales/answer-a-security-questionnaire.md)
- **Route What the Records Cannot Answer**
  - `ref/fin/respond-to-a-tax-audit`, activity 9 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
  - `ref/fin/run-the-external-audit`, activity 7 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
  - `ref/hr/respond-to-an-employment-audit`, activity 9 -
    [Respond to an Employment Audit](../../../../processes/human-resources/respond-to-an-employment-audit.md)
- **Route the Unanswered Questions**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 7 -
    [Answer a Due Diligence Questionnaire](../../../../processes/private-capital/answer-a-due-diligence-questionnaire.md)

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
