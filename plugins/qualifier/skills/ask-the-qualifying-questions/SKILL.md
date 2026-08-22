---
name: ask-the-qualifying-questions
description: Writes the questions down before anybody asks them, then works with the seller through the problem, the money, the decision, the date and the alternatives. Use it when running `ref/sls/qualify-an-opportunity`.
license: CC-BY-4.0
metadata:
  agent: qualifier
  agent-version: "1"
---

# Ask the qualifying questions

## What it does

Writes the questions down before anybody asks them, then works with the
seller through the problem, the money, the decision, the date and the
alternatives. Every answer is recorded in the words it came back in, or
marked unanswered, unclear, contradicted or declined.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Ask About the Decision**
  - `ref/sls/qualify-an-opportunity`, activity 7 -
    [Qualify an Opportunity](../../../../processes/sales/qualify-an-opportunity.md)
- **Ask About the Problem**
  - `ref/sls/qualify-an-opportunity`, activity 5 -
    [Qualify an Opportunity](../../../../processes/sales/qualify-an-opportunity.md)
- **Write the Questions to Ask**
  - `ref/sls/qualify-an-opportunity`, activity 4 -
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
