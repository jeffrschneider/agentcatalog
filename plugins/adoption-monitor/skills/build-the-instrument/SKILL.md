---
name: build-the-instrument
description: Names the departures no system would show today, designs the fields, events and logs that would have to change to show them, and builds them once the change has been signed. Use it when running `ref/rev/instrument-a-process`.
license: CC-BY-4.0
metadata:
  agent: adoption-monitor
  agent-version: "1"
---

# Build the instrument

## What it does

Names the departures no system would show today, designs the fields,
events and logs that would have to change to show them, and builds them
once the change has been signed.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Build the Fields and the Events**
  - `ref/rev/instrument-a-process`, activity 9 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)
- **Design the System Changes**
  - `ref/rev/instrument-a-process`, activity 6 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)
- **Name the Signals That Are Missing**
  - `ref/rev/instrument-a-process`, activity 5 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)

## What to record

Per process: the watched steps, and the unwatched ones with the reason
each was left out. For each watched step, the observable difference
between a followed run and a departed one. The change request field by
field, saying what each new field records about a person, and the policy
check with the line behind every refusal and the fields the privacy
reviewer struck out. The baseline, and the detection's score against the
known runs with every miss and every false alarm listed. Every signal
raised in the first weeks, checked by hand against the run it fired on.
The steps it still cannot see. Per period: the measure's gaps and
outages marked before a number is read, the ranked departures with the
count behind each rate, and what people said, attributed to a role, with
the refusals counted as refusals.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
