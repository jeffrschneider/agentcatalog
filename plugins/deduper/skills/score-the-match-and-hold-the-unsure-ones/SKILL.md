---
name: score-the-match-and-hold-the-unsure-ones
description: Scores how sure the match is, keeping the model version and the inputs beside the score, and sends anything under the bar to a person rather than merging it. Use it when running `ref/rev/dedupe-and-merge`.
license: CC-BY-4.0
metadata:
  agent: deduper
  agent-version: "1"
---

# Score the match and hold the unsure ones

## What it does

Scores how sure the match is, keeping the model version and the inputs
beside the score, and sends anything under the bar to a person rather
than merging it. Deciding that two records are one thing is never this
agent's call.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Route the Unsure Ones to a Person**
  - `ref/rev/dedupe-and-merge`, activity 5 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Score the Match**
  - `ref/rev/dedupe-and-merge`, activity 4 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)

## What to record

Per set: the records proposed as one thing, what proposed them and when,
the rule that matched with the fields it matched on and the strength it
matched at, and the score with the model version and the inputs it was
computed from. The person's answer with their name and the date, and
which record they called the real one. The surviving id and the reason
it was chosen over the other. Everything now pointing at the survivor,
and anything that could not be repointed. Both owners told, with the
date they were told. The merge as written, and the closed record
pointing at the survivor. Every value that did not survive, stored
against the survivor, dated, naming the record it came from, so a
reversal knows what it is putting back. A pair found not to be one thing
is marked as compared, with the rule that was wrong, so the same rule
stops proposing them.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
