---
name: move-work-that-reached-the-wrong-person
description: Takes a report that work went to the wrong person, confirms it, works out who should have had it, and moves it. Use it when running `ref/rev/fix-a-misroute`.
license: CC-BY-4.0
metadata:
  agent: routing-keeper
  agent-version: "1"
---

# Move work that reached the wrong person

## What it does

Takes a report that work went to the wrong person, confirms it, works
out who should have had it, and moves it. Both people are told, whatever
the wrong receiver already promised is written down, and every other
item the same clause placed the same way is moved with it.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Confirm It Went to the Wrong Person**
  - `ref/rev/fix-a-misroute`, activity 2 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Find Who Should Have Got It**
  - `ref/rev/fix-a-misroute`, activity 4 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Move the Ones That Are Also Wrong**
  - `ref/rev/fix-a-misroute`, activity 13 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Move the Work**
  - `ref/rev/fix-a-misroute`, activity 5 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Record What Already Happened**
  - `ref/rev/fix-a-misroute`, activity 7 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Take in the Report of a Misroute**
  - `ref/rev/fix-a-misroute`, activity 1 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Tell Both People**
  - `ref/rev/fix-a-misroute`, activity 6 -
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
