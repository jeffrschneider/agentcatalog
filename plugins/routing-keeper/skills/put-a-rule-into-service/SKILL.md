---
name: put-a-rule-into-service
description: Builds the signed rule into the system that hands out the work, checks where the first items actually land, publishes the copy people are held to, and tells everyone the change reaches what is different now. Use it when running `ref/rev/write-a-routing-rule`.
license: CC-BY-4.0
metadata:
  agent: routing-keeper
  agent-version: "1"
---

# Put a rule into service

## What it does

Builds the signed rule into the system that hands out the work, checks
where the first items actually land, publishes the copy people are held
to, and tells everyone the change reaches what is different now.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Announce What Changes**
  - `ref/rev/write-a-routing-rule`, activity 16 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Implement the Rule**
  - `ref/rev/write-a-routing-rule`, activity 13 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Publish the Rule Where People Read It**
  - `ref/rev/write-a-routing-rule`, activity 15 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Verify It in the Live System**
  - `ref/rev/write-a-routing-rule`, activity 14 -
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
