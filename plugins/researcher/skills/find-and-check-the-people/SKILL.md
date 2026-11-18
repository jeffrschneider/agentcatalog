---
name: find-and-check-the-people
description: Finds candidates for a role at a portfolio company beyond the people the firm already knows, and builds one long list with each candidate on it once and where each one came from. Use it when running `ref/pc/fill-a-key-role-at-a-portfolio-company` and `ref/pc/run-commercial-and-product-diligence`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Find and check the people

## What it does

Finds candidates for a role at a portfolio company beyond the people the
firm already knows, and builds one long list with each candidate on it
once and where each one came from. It takes the references on a
management team in diligence and on a chosen candidate, runs a
candidate's background checks only with the candidate's written consent,
and records where the hire came from and what the search took.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Long List**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 8 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Check the Management Team**
  - `ref/pc/run-commercial-and-product-diligence`, activity 13 -
    [Run Commercial and Product Diligence](../../../../processes/private-capital/run-commercial-and-product-diligence.md)
- **Find Candidates Outside the Network**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 7 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Record the Search**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 18 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Run the Background Checks**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 14 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Take the References**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 13 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
