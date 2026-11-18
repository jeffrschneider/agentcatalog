---
name: check-the-figures-against-the-record
description: Reads every performance figure in the answers against the frozen track record at its version, with the gross figure and the net figure side by side, and every claim against the advertising rules, beside the chief compliance officer. Use it when running `ref/pc/answer-a-due-diligence-questionnaire`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Check the figures against the record

## What it does

Reads every performance figure in the answers against the frozen track
record at its version, with the gross figure and the net figure side by
side, and every claim against the advertising rules, beside the chief
compliance officer. A figure that does not match goes back to be drafted
again from the record, because every investor must see the same numbers.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check the Figures and the Claims**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 10 -
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
