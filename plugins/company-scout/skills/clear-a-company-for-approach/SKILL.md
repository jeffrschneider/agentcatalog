---
name: clear-a-company-for-approach
description: Takes in a ready company and checks that nobody at the firm is already talking to it, and that no do-not-contact request, restricted list entry, standstill or portfolio conflict bars an approach. Use it when running `ref/pc/reach-out-to-a-company`.
license: CC-BY-4.0
metadata:
  agent: company-scout
  agent-version: "1"
---

# Clear a company for approach

## What it does

Takes in a ready company and checks that nobody at the firm is already
talking to it, and that no do-not-contact request, restricted list
entry, standstill or portfolio conflict bars an approach.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check Nobody Is Already Talking**
  - `ref/pc/reach-out-to-a-company`, activity 2 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)
- **Check the Company May Be Approached**
  - `ref/pc/reach-out-to-a-company`, activity 3 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)
- **Take in the Ready Company**
  - `ref/pc/reach-out-to-a-company`, activity 1 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)

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
