---
name: calculate-the-returns
description: Calculates the internal rate of return (IRR) and the multiples, gross and net, by deal and by fund for the track record and for each quarter, and attributes each deal's gain, treating the losses the same way as the gains. Use it when running `ref/pc/issue-the-quarterly-report-and-statements` and `ref/pc/prepare-the-fundraising-materials`.
license: CC-BY-4.0
metadata:
  agent: performance-calculator
  agent-version: "1"
---

# Calculate the returns

## What it does

Calculates the internal rate of return (IRR) and the multiples, gross
and net, by deal and by fund for the track record and for each quarter,
and attributes each deal's gain, treating the losses the same way as the
gains.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Attribute Each Deal's Gain**
  - `ref/pc/prepare-the-fundraising-materials`, activity 5 -
    [Prepare the Fundraising Materials](../../../../processes/private-capital/prepare-the-fundraising-materials.md)
- **Calculate the Fund's Performance**
  - `ref/pc/issue-the-quarterly-report-and-statements`, activity 8 -
    [Issue the Quarterly Report and Statements](../../../../processes/private-capital/issue-the-quarterly-report-and-statements.md)
- **Calculate the Track Record**
  - `ref/pc/prepare-the-fundraising-materials`, activity 4 -
    [Prepare the Fundraising Materials](../../../../processes/private-capital/prepare-the-fundraising-materials.md)

## What to record

Each run starts from the performance method at a version, written and
dated before any figure, naming which deals and funds are included, how
fees, carried interest and any credit line are treated, and the date the
figures are taken at. Every deal's dated cash flows and its mark are
recorded with their source. The track record gives the IRR and each
multiple by deal and by fund, gross and net side by side, and the
attribution of each deal's gain, with the losses attributed the same
way. Each figure is traced to the audited statements, or to the books
where the audit does not reach, with every difference and its
explanation. The frozen set carries its date and version, and the run
records which documents were told to use it. The method, the workpapers,
the approvals and every version sent are kept for the retention period.
Each quarter leaves the IRR and the multiples for the fund and for each
holding, gross and net, with the effect of the credit line shown and the
method version named. Any figure can be recomputed from the recorded
cash flows, marks and method.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
