---
name: plan-new-content
description: Takes in each request for an article or a saved reply, reads the replies already saved on the same question, finds the approved content a reply will rest on, and plans each article from the customers' own words with its readers, its plans and its owner. Use it when running `ref/sup/publish-a-saved-reply` and `ref/sup/write-a-help-article`.
license: CC-BY-4.0
metadata:
  agent: knowledge-keeper
  agent-version: "1"
---

# Plan new content

## What it does

Takes in each request for an article or a saved reply, reads the replies
already saved on the same question, finds the approved content a reply
will rest on, and plans each article from the customers' own words with
its readers, its plans and its owner.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Find the Approved Content Behind It**
  - `ref/sup/publish-a-saved-reply`, activity 3 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Plan the Article**
  - `ref/sup/write-a-help-article`, activity 2 -
    [Write a Help Article](../../../../processes/customer-support/write-a-help-article.md)
- **Read the Replies Already Saved**
  - `ref/sup/publish-a-saved-reply`, activity 2 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Take In the Request**
  - `ref/sup/write-a-help-article`, activity 1 -
    [Write a Help Article](../../../../processes/customer-support/write-a-help-article.md)
- **Take In the Request for a Reply**
  - `ref/sup/publish-a-saved-reply`, activity 1 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)

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
