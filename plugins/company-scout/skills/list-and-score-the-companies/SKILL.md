---
name: list-and-score-the-companies
description: Lists every company that meets the criteria with the source it was found in, scores each one with the reason it fits and the facts still missing, matches the list to what the firm already holds, and issues the map with its watch list at a version, adding a company found later at a new version. Use it when running `ref/pc/map-a-sector`.
license: CC-BY-4.0
metadata:
  agent: company-scout
  agent-version: "1"
---

# List and score the companies

## What it does

Lists every company that meets the criteria with the source it was found
in, scores each one with the reason it fits and the facts still missing,
matches the list to what the firm already holds, and issues the map with
its watch list at a version, adding a company found later at a new
version.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Add a Company Found Later**
  - `ref/pc/map-a-sector`, activity 15 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **Agree Which Companies to Watch**
  - `ref/pc/map-a-sector`, activity 10 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **Issue the Map at a Version**
  - `ref/pc/map-a-sector`, activity 11 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **List the Companies That Fit**
  - `ref/pc/map-a-sector`, activity 7 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **Match the List to What the Firm Holds**
  - `ref/pc/map-a-sector`, activity 9 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)
- **Say Why Each Company Fits**
  - `ref/pc/map-a-sector`, activity 8 -
    [Map a Sector](../../../../processes/private-capital/map-a-sector.md)

## What to record

The sector proposal with its owning partner and why it is worth mapping
now. The thesis at its version, with each claim marked held, weakened or
dropped and the source that settled it. The fit check against the fund's
strategy and limits at their version, with the clause behind any
failure. The criteria at the version they were fixed at, before any
company was scored. Per company: the source it was found in and the date
that source was read, its score against the criteria with the reason it
fits and the facts still missing, and what the CRM and the pipeline held
on it. The watch list with one owning partner per company, and the
companies set aside with the reason. The map at each version with its
review date, and each company added later at the version that added it.
Each sign recorded with its source and date, and each ready company
passed on with the sign, the case and the day it reached its partner.
Per approach: the open-thread check, the check of the do-not-contact
list, the restricted list, any standstill and any portfolio conflict,
each dated; the approach as written and the person who sent it; the
follow-up date; the partner's decision with its reason; the opportunity
opened with its owner; and the outcome. At review: keep, refresh or
retire with the reason, and the approaches, meetings and deals the map
led to, with the companies it missed. An auditor can take any company on
the map and see why it was there, who owned it, and every time the firm
reached out to it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
