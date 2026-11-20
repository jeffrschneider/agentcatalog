---
name: carry-a-release-back
description: Takes in a released request with its version and plans, lists every account that asked with its case and whether its plan has the feature, and records a release that misses the need in the customer's own words. Use it when running `ref/sup/tell-customers-about-a-fix`.
license: CC-BY-4.0
metadata:
  agent: feedback-keeper
  agent-version: "1"
---

# Carry a release back

## What it does

Takes in a released request with its version and plans, lists every
account that asked with its case and whether its plan has the feature,
and records a release that misses the need in the customer's own words.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **List the Customers Who Asked**
  - `ref/sup/tell-customers-about-a-fix`, activity 4 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Record a Release That Misses the Need**
  - `ref/sup/tell-customers-about-a-fix`, activity 12 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Take In a Released Request**
  - `ref/sup/tell-customers-about-a-fix`, activity 2 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)

## What to record

Each request leaves the ask in the customer's own words with what they
are trying to get done and what they do today instead, the check that
the product does not already do it with the specialist who confirmed it,
the need as written with any solution the customer suggested kept beside
it, the search of the requests already logged with each likely match and
why, the request logged or joined with its reference, every account
counted with its plan and what it pays, the approved wording the
customer was sent and when, each question from the product team with the
customer's answer, and the case marked with the request. Each release
leaves the version and the plans that include it, every account that
asked with its case and whether its plan has the feature, and each need
the release missed in the customer's own words. Each period leaves the
open requests counted, the topic list at its version with any new topic
named, the cases, counts and quotes under each finding, carrying the
case reference and the account and no individual's contact details, and
each decision on a request with its owner and its date. Nothing in the
record shows this agent deciding what is built, promising a request or
giving a date, quoting a case about a person's own data, a security
report or a legal matter, or naming a support specialist in a finding.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
