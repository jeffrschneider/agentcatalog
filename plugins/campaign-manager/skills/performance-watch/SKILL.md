---
name: performance-watch
description: Tracks a run while it is live and sets what is coming back against what the brief promised, including the responses that ought to worry somebody, such as complaints and opt-outs. Use it when running `ref/mkt/co-marketing-campaign`, `ref/mkt/social-campaign` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Performance watch

## What it does

Tracks a run while it is live and sets what is coming back against what
the brief promised, including the responses that ought to worry
somebody, such as complaints and opt-outs.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Watch Performance**
  - `ref/mkt/social-campaign`, activity 9 -
    [Run Social Media Campaign](../../../../processes/marketing/social-campaign.md)
- **Watch the Joint Campaign**
  - `ref/mkt/co-marketing-campaign`, activity 13 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Watch the Response**
  - `ref/mkt/win-back-campaign`, activity 17 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
