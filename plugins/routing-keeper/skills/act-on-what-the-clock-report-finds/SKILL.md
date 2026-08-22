---
name: act-on-what-the-clock-report-finds
description: Sits with the people who own a clock to fix what that clock covers, and opens the rule work a published clock report calls for. Use it when running `ref/rev/watch-the-response-clock`.
license: CC-BY-4.0
metadata:
  agent: routing-keeper
  agent-version: "1"
---

# Act on what the clock report finds

## What it does

Sits with the people who own a clock to fix what that clock covers, and
opens the rule work a published clock report calls for.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Name What Each Clock Covers**
  - `ref/rev/watch-the-response-clock`, activity 2 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Open the Work the Report Calls For**
  - `ref/rev/watch-the-response-clock`, activity 15 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)

## What to record

Per rule: the rule in plain sentences at a version, the precedence
between clauses, the named owner for anything unmatched, the volume each
clause sends against what each receiving queue holds, every objection
the receivers raised with the answer to it and the name of anyone who
overruled one, the replay against past records with every record the
rule would have sent elsewhere, and the signature naming the person and
the version. The configuration records the rule version it was built
from, and the live check records where the first items actually landed.
Per misroute: the rule version and the clause that matched, the value
the field held at the time of routing, the move with its reason, who was
told and when, what the wrong receiver had already promised, the one
named cause, and how many other items the same clause placed the same
way.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
