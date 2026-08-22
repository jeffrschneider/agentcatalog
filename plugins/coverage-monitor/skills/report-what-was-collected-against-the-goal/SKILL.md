---
name: report-what-was-collected-against-the-goal
description: Sets the coverage it collected beside what the run was meant to achieve and reports where the two agree and where they do not. Use it when running `ref/mkt/announce-company-news` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: coverage-monitor
  agent-version: "1"
---

# Report what was collected against the goal

## What it does

Sets the coverage it collected beside what the run was meant to achieve
and reports where the two agree and where they do not.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Report Whether the Positioning Landed**
  - `ref/mkt/brief-industry-analyst`, activity 16 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
- **Report on the Announcement**
  - `ref/mkt/announce-company-news`, activity 16 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
- **Report the Conference**
  - `ref/mkt/user-conference`, activity 16 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Report the Result**
  - `ref/mkt/speaking-engagement`, activity 15 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)

## What to record

One entry per mention, giving the outlet, the date it appeared, the
author, the headline, the address it lives at, and what the piece said
about the organization, quoted where the exact wording matters. Each
entry says whether the mention can be traced back to something the
organization sent out. A summary at the cadence the process sets,
covering what ran, where it ran, and how the tone moved since the last
one. A source it could not reach appears in the summary as unreached.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
