---
name: log-what-appears-while-a-run-is-live
description: Watches the named sources while a run is in flight and records each thing that appears, whether it is an article, a post, an analyst note, a review or a result, keeping the wording and where it ran. Use it when running `ref/mkt/announce-company-news` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: coverage-monitor
  agent-version: "1"
---

# Log what appears while a run is live

## What it does

Watches the named sources while a run is in flight and records each
thing that appears, whether it is an article, a post, an analyst note, a
review or a result, keeping the wording and where it ran.

## Where it happens

The agent does this in six activities across seven reference processes.
Each one names the activity as that process words it.

- **Log the Coverage**
  - `ref/mkt/pitch-earned-media`, activity 14 -
    [Pitch Earned Media](../../../../processes/marketing/pitch-earned-media.md)
- **Record the Live Posts**
  - `ref/mkt/influencer-campaign`, activity 14 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)
- **Track the Coverage**
  - `ref/mkt/announce-company-news`, activity 15 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
  - `ref/mkt/crisis-communication`, activity 13 -
    [Manage Crisis Communication](../../../../processes/marketing/crisis-communication.md)
- **Track the Result**
  - `ref/mkt/award-entry`, activity 14 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
- **Watch What Gets Published**
  - `ref/mkt/brief-industry-analyst`, activity 14 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
- **Watch the Reviews Land**
  - `ref/mkt/customer-reviews`, activity 13 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)

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
