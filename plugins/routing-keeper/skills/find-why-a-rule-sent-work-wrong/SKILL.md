---
name: find-why-a-rule-sent-work-wrong
description: Names one cause for a misroute and says whether the data or the rule produced it. Use it when running `ref/rev/fix-a-misroute`.
license: CC-BY-4.0
metadata:
  agent: routing-keeper
  agent-version: "1"
---

# Find why a rule sent work wrong

## What it does

Names one cause for a misroute and says whether the data or the rule
produced it. Raises the change the rule needs and files the case against
the version of the rule that ran.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **File the Case Against the Rule**
  - `ref/rev/fix-a-misroute`, activity 14 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Find Why the Rule Sent It Wrong**
  - `ref/rev/fix-a-misroute`, activity 8 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Raise the Rule Change**
  - `ref/rev/fix-a-misroute`, activity 11 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Say Whether It Is the Data or the Rule**
  - `ref/rev/fix-a-misroute`, activity 9 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)

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
