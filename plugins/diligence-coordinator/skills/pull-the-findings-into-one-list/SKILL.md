---
name: pull-the-findings-into-one-list
description: Brings every specialist's finding into one rated list with an owner and a date against each, names every claim that stayed unproved as unproved rather than dropping it, and reports go, go with conditions or stop to the sponsor with the cut scope attached. Use it when running `ref/pc/run-commercial-and-product-diligence` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: diligence-coordinator
  agent-version: "1"
---

# Pull the findings into one list

## What it does

Brings every specialist's finding into one rated list with an owner and
a date against each, names every claim that stayed unproved as unproved
rather than dropping it, and reports go, go with conditions or stop to
the sponsor with the cut scope attached.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Decide What Each Finding Needs**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 18 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **List the Findings**
  - `ref/pc/run-commercial-and-product-diligence`, activity 15 -
    [Run Commercial and Product Diligence](../../../../processes/private-capital/run-commercial-and-product-diligence.md)
  - `ref/pc/run-financial-diligence`, activity 14 -
    [Run Financial Diligence](../../../../processes/private-capital/run-financial-diligence.md)
  - `ref/pc/run-legal-and-compliance-diligence`, activity 17 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
  - `ref/prt/run-alliance-diligence`, activity 15 -
    [Run Alliance Diligence](../../../../processes/partners/run-alliance-diligence.md)
- **Report to the Deal Lead**
  - `ref/pc/run-commercial-and-product-diligence`, activity 16 -
    [Run Commercial and Product Diligence](../../../../processes/private-capital/run-commercial-and-product-diligence.md)
- **Report to the Sponsor**
  - `ref/prt/run-alliance-diligence`, activity 17 -
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
