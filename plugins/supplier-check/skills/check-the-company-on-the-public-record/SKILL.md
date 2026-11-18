---
name: check-the-company-on-the-public-record
description: The agent reads the registries for a company's registration, its good standing and who owns it, and reads the court and regulator records for suits, threats, regulator letters and settlements beside outside counsel. Use it when running `ref/pc/run-legal-and-compliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: supplier-check
  agent-version: "1"
---

# Check the company on the public record

## What it does

The agent reads the registries for a company's registration, its good
standing and who owns it, and reads the court and regulator records for
suits, threats, regulator letters and settlements beside outside
counsel. Each result names the record it came from and the date it was
read.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Company Is Real**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 5 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Read the Litigation and Claims**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 11 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)

## What to record

It leaves a scoring sheet for each candidate at a version, naming the
requirements list and the version it scored against, with one row per
requirement carrying the verdict and the evidence behind it. The
evidence names the demonstration step, the document, or the reference
call it came from, so a person can check a verdict without asking the
agent what it meant. A requirement it could not test is recorded as not
tested, with the reason it could not be tested. When a candidate revises
its material, the rescore says what changed, what was run again, and
what was carried over from the earlier score. It records the date each
candidate's material arrived and the date it was scored.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
