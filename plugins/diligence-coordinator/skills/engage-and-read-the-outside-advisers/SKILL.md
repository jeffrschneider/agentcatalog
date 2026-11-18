---
name: engage-and-read-the-outside-advisers
description: Sets the scope, the timetable and the fee for each outside adviser the deal lead engages, whether a commercial adviser, the accountants or outside counsel, and has the engagement letter ready for the deal lead to sign before any work starts. Use it when running `ref/pc/run-commercial-and-product-diligence`, `ref/pc/run-financial-diligence` and `ref/pc/run-legal-and-compliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: diligence-coordinator
  agent-version: "1"
---

# Engage and read the outside advisers

## What it does

Sets the scope, the timetable and the fee for each outside adviser the
deal lead engages, whether a commercial adviser, the accountants or
outside counsel, and has the engagement letter ready for the deal lead
to sign before any work starts. It then reads each adviser's report
against the claims to prove and the team's own findings, and keeps every
difference on the record with both sources, because an adviser's
conclusion is evidence to test like any other.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Engage Outside Counsel**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 3 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Engage the Commercial Adviser**
  - `ref/pc/run-commercial-and-product-diligence`, activity 5 -
    [Run Commercial and Product Diligence](../../../../processes/private-capital/run-commercial-and-product-diligence.md)
- **Engage the Outside Accountants**
  - `ref/pc/run-financial-diligence`, activity 4 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Accountants' Report**
  - `ref/pc/run-financial-diligence`, activity 13 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
- **Read the Adviser's Report**
  - `ref/pc/run-commercial-and-product-diligence`, activity 14 -
    [Run Commercial and Product Diligence](../../../../processes/private-capital/run-commercial-and-product-diligence.md)

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
