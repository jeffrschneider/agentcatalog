---
name: return-a-lead-to-nurture
description: Takes a decision not to work a lead now, reads the reason given, and checks it against what the record actually says. Use it when running `ref/sls/return-a-lead-to-nurture`.
license: CC-BY-4.0
metadata:
  agent: qualifier
  agent-version: "1"
---

# Return a lead to nurture

## What it does

Takes a decision not to work a lead now, reads the reason given, and
checks it against what the record actually says. Names the events that
would end the wait early, writes the handback note, closes the
opportunity record, and records what the wait eventually produced.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Check the Reason Against the Record**
  - `ref/sls/return-a-lead-to-nurture`, activity 3 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Close the Opportunity Record**
  - `ref/sls/return-a-lead-to-nurture`, activity 10 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Name What Would Bring It Back Early**
  - `ref/sls/return-a-lead-to-nurture`, activity 5 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Read the Reason Given**
  - `ref/sls/return-a-lead-to-nurture`, activity 2 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Record the Outcome**
  - `ref/sls/return-a-lead-to-nurture`, activity 13 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Take in the Return Decision**
  - `ref/sls/return-a-lead-to-nurture`, activity 1 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)
- **Write the Handback Note**
  - `ref/sls/return-a-lead-to-nurture`, activity 6 -
    [Return a Lead to Nurture](../../../../processes/sales/return-a-lead-to-nurture.md)

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
