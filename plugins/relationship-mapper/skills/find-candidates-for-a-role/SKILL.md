---
name: find-candidates-for-a-role
description: Finds the people the firm already knows who fit a role's specification, with how well the firm knows each one and the path to each, and puts them with the candidates from research into one long list where each person appears once with the source they came from. Use it when running `ref/hr/find-candidates` and `ref/pc/fill-a-key-role-at-a-portfolio-company`.
license: CC-BY-4.0
metadata:
  agent: relationship-mapper
  agent-version: "1"
---

# Find candidates for a role

## What it does

Finds the people the firm already knows who fit a role's specification,
with how well the firm knows each one and the path to each, and puts
them with the candidates from research into one long list where each
person appears once with the source they came from. Records where the
hire came from and what the search took, so the next search starts from
it.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Long List**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 8 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Find Candidates in the Firm's Network**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 6 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)
- **Record What the Search Taught**
  - `ref/hr/find-candidates`, activity 18 -
    [Find Candidates](../../../../processes/human-resources/find-candidates.md)
- **Record the Search**
  - `ref/pc/fill-a-key-role-at-a-portfolio-company`, activity 18 -
    [Fill a Key Role at a Portfolio Company](../../../../processes/private-capital/fill-a-key-role-at-a-portfolio-company.md)

## What to record

Per person: the decision they sit under, whether they decide, influence,
block or use, the source they were found in and that source's
publication date, the reporting line behind any claim of authority, the
strength score with the contact history it was computed from, the path
in and who at our end holds it, and the stance with what was said or
done behind it. Per map: every decision with no decider found or nobody
we know marked as a gap rather than left blank, what the privacy check
removed and the rule behind each removal, and the issued version naming
who corrected what and when they signed. A claim that somebody knows a
buyer well is recorded as a claim, with the person who made it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
