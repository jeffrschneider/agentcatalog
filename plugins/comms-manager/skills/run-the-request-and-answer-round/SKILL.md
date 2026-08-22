---
name: run-the-request-and-answer-round
description: The agent runs a round where every function submits what it is asking for in one format by one date, and then tells each function what it was given and the rules that come with it. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: comms-manager
  agent-version: "1"
---

# Run the request and answer round

## What it does

The agent runs a round where every function submits what it is asking
for in one format by one date, and then tells each function what it was
given and the rules that come with it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Collect What Each Function Asks For**
  - `ref/mkt/set-marketing-budget`, activity 4 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Tell Every Function What It Has**
  - `ref/mkt/set-marketing-budget`, activity 14 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

The timeline at a version, saying what was known at each point, who
established it, and who was told. Each audience's wording at the version
that actually went out, with the versions it replaced left where they
are. The CONVENED and DONE records of everything it convenes. The go
record, naming the person who said go and the time they said it. The
report afterwards, setting what happened against what the announcement
or the response was meant to do.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
