---
name: clear-the-traffic
description: Other tests and changes due on the same visitors. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Clear the Traffic

## What happens

Other tests and changes due on the same visitors.

## Where it happens

- `ref/mkt/conversion-experiment`, activity 4 -
  [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

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
