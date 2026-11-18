---
name: add-the-new-answers-to-the-library
description: Adds each answer its owner signed to the library at a version, with the owner, the source behind it and the date it must be read again, so the next questionnaire draws on it rather than asking the owner twice. Use it when running `ref/pc/answer-a-due-diligence-questionnaire`.
license: CC-BY-4.0
metadata:
  agent: questionnaire-responder
  agent-version: "1"
---

# Add the new answers to the library

## What it does

Adds each answer its owner signed to the library at a version, with the
owner, the source behind it and the date it must be read again, so the
next questionnaire draws on it rather than asking the owner twice.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Add the New Answers to the Library**
  - `ref/pc/answer-a-due-diligence-questionnaire`, activity 15 -
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
