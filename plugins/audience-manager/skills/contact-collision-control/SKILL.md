---
name: contact-collision-control
description: Keeps the same people from being hit too hard or by two things at once, by setting how often one person may see something and for how long, and by reading what else is already due on the same contacts. Use it when running `ref/mkt/conversion-experiment` and `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Contact collision control

## What it does

Keeps the same people from being hit too hard or by two things at once,
by setting how often one person may see something and for how long, and
by reading what else is already due on the same contacts.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Clear the Traffic**
  - `ref/mkt/conversion-experiment`, activity 4 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Set the Exposure Rules**
  - `ref/mkt/display-retargeting`, activity 11 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)

## What to record

Each program at a version, naming the entry condition, every step, every
wait, the condition on every branch, and every exit. The hygiene cycle's
scope at a version, saying which records it covers and what it has to
fix in them. The rule that settles which program takes a contact who
qualifies for two, with the date it was decided and who decided it. A
dated account of the database between cycles: how many records there
are, how many are complete enough to use, and how many may be contacted.
The CONVENED and DONE records of everything it convenes. The go record
for a program, naming the version that started sending and who said go.
The standing readout at the cadence the process sets, and the decision
it made after reading it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
