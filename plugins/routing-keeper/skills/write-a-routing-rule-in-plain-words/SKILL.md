---
name: write-a-routing-rule-in-plain-words
description: Takes the question of who should get what, reads how the work is routed now, and writes the answer as sentences a seller can read without training. Use it when running `ref/rev/write-a-routing-rule`.
license: CC-BY-4.0
metadata:
  agent: routing-keeper
  agent-version: "1"
---

# Write a routing rule in plain words

## What it does

Takes the question of who should get what, reads how the work is routed
now, and writes the answer as sentences a seller can read without
training. Sets which clause wins where two could match, and names the
person anything unmatched goes to.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Name Who Should Get What**
  - `ref/rev/write-a-routing-rule`, activity 3 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Read How Work Is Routed Now**
  - `ref/rev/write-a-routing-rule`, activity 2 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Set the Order and the Fallback**
  - `ref/rev/write-a-routing-rule`, activity 7 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Take in the Routing Question**
  - `ref/rev/write-a-routing-rule`, activity 1 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Write the Rule in Plain Words**
  - `ref/rev/write-a-routing-rule`, activity 6 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)

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
