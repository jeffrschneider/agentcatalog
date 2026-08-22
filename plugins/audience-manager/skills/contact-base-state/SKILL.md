---
name: contact-base-state
description: Says what state the contact base is in, giving the counts, the gaps, the duplicates, the bounces and the records that have to come out with the reason for each, and reports after a cycle what changed and how much of the base can still be reached. Use it when running `ref/mkt/contact-database-hygiene`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Contact base state

## What it does

Says what state the contact base is in, giving the counts, the gaps, the
duplicates, the bounces and the records that have to come out with the
reason for each, and reports after a cycle what changed and how much of
the base can still be reached.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **List What Comes Out**
  - `ref/mkt/contact-database-hygiene`, activity 9 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- **Measure the Base as It Stands**
  - `ref/mkt/contact-database-hygiene`, activity 2 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- **Report the Cycle**
  - `ref/mkt/contact-database-hygiene`, activity 16 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)

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
