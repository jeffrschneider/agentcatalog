---
name: find-the-gaps
description: Collects each period's questions the agents could not answer, groups every source into one gap for each topic, ranks the gaps by the customers each touches, starts an article for each gap the knowledge lead chooses, passes on what an article cannot fix, and publishes the ranked list. Use it when running `ref/sup/find-gaps-in-the-help-center`.
license: CC-BY-4.0
metadata:
  agent: knowledge-keeper
  agent-version: "1"
---

# Find the gaps

## What it does

Collects each period's questions the agents could not answer, groups
every source into one gap for each topic, ranks the gaps by the
customers each touches, starts an article for each gap the knowledge
lead chooses, passes on what an article cannot fix, and publishes the
ranked list.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Collect the Questions the Agents Could Not Answer**
  - `ref/sup/find-gaps-in-the-help-center`, activity 5 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Group the Gaps by Topic**
  - `ref/sup/find-gaps-in-the-help-center`, activity 6 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Open the Period**
  - `ref/sup/find-gaps-in-the-help-center`, activity 1 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Pass On What an Article Cannot Fix**
  - `ref/sup/find-gaps-in-the-help-center`, activity 13 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Publish the Ranked List**
  - `ref/sup/find-gaps-in-the-help-center`, activity 14 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Rank the Gaps**
  - `ref/sup/find-gaps-in-the-help-center`, activity 10 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Start an Article for Each Chosen Gap**
  - `ref/sup/find-gaps-in-the-help-center`, activity 12 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)

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
