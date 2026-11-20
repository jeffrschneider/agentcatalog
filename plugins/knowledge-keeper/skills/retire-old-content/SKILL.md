---
name: retire-old-content
description: Takes down each article or saved reply that has been replaced or retired, sends its address to the closest article, moves every link to it, and keeps the old version with the dates it was in use. Use it when running `ref/sup/publish-a-saved-reply`, `ref/sup/review-the-help-center` and `ref/sup/write-a-help-article`.
license: CC-BY-4.0
metadata:
  agent: knowledge-keeper
  agent-version: "1"
---

# Retire old content

## What it does

Takes down each article or saved reply that has been replaced or
retired, sends its address to the closest article, moves every link to
it, and keeps the old version with the dates it was in use.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Retire the Version It Replaces**
  - `ref/sup/publish-a-saved-reply`, activity 14 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Take Down Retired Articles**
  - `ref/sup/review-the-help-center`, activity 10 -
    [Review the Help Center](../../../../processes/customer-support/review-the-help-center.md)
- **Take Down What It Replaces**
  - `ref/sup/write-a-help-article`, activity 11 -
    [Write a Help Article](../../../../processes/customer-support/write-a-help-article.md)

## What to record

Each article leaves the request, the plan with the customers' own words,
the cases and searches behind it and its owner, the version published
with who approved it and its review date, what it replaced with every
link moved, and the moment it joined the list the agents answer from.
Each saved reply leaves the replies already saved on the question, the
content it rests on at its versions, the mark for who may send it and
any mark for approval, the version it retired with the dates that
version was in use, and what the team was told. Each review leaves the
articles opened with their owners, what the cases said, the findings and
the proposal for each article, each owner's decision, each article taken
off the list and the day it came off, and the list as changed. Each gap
period leaves every source read or shown as unread, the gaps with their
evidence and their rank, the knowledge lead's choices and the runs they
opened. Each release leaves what it changes, every article and reply it
touches with its state on the date, the moment each went live and the
content it replaced came off the list, and the questions of its first
days. Each routine question leaves the content matched with its version,
or the gap recorded in the customer's words. Nothing in the record shows
this agent approving content, publishing a version no owner approved, or
keeping content on the list after it was found wrong.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
