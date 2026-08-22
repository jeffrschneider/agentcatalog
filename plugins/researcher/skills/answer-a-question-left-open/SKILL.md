---
name: answer-a-question-left-open
description: Goes back after a meeting or a conversation and settles the questions nobody could answer at the time. Use it when running `ref/mkt/brief-executive-leadership`, `ref/mkt/brief-industry-analyst` and `ref/mkt/pitch-earned-media`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Answer a question left open

## What it does

Goes back after a meeting or a conversation and settles the questions
nobody could answer at the time. It finds the extra data, runs the fact
check, or arranges the further interview, and returns the answer with
its source.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Answer What Reporters Ask**
  - `ref/mkt/pitch-earned-media`, activity 13 -
    [Pitch Earned Media](../../../../processes/marketing/pitch-earned-media.md)
- **Answer What Was Left Open**
  - `ref/mkt/brief-executive-leadership`, activity 18 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
  - `ref/mkt/brief-industry-analyst`, activity 13 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
