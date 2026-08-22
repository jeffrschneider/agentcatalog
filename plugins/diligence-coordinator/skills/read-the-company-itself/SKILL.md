---
name: read-the-company-itself
description: Reads the financial position, naming revenue, runway and how concentrated the revenue is, and establishes who owns anything the company would embed or resell. Use it when running `ref/prt/run-alliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: diligence-coordinator
  agent-version: "1"
---

# Read the company itself

## What it does

Reads the financial position, naming revenue, runway and how
concentrated the revenue is, and establishes who owns anything the
company would embed or resell.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check Who Owns the Technology**
  - `ref/prt/run-alliance-diligence`, activity 12 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)
- **Read the Financial Position**
  - `ref/prt/run-alliance-diligence`, activity 6 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)

## What to record

The thesis at its version, with every claim it assumes written out as a
thing to be proved. What was in scope and what was cut, named as cut.
The access agreement, saying who gives what, to whom, and by when. The
numbered request log: each request, who it went to, when it was
answered, and what the answer was. The financial reading, naming
revenue, runway and how concentrated the revenue is. The ownership
finding on anything the company would embed or resell. Every finding
rated on the scale in force, with an owner and a date. Every claim that
stayed unproved, named as unproved rather than dropped. The report to
the sponsor, naming go, go with conditions or stop, and listing every
area that was cut from scope.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
