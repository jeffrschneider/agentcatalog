---
name: contact-coordination
description: Settles who approaches which account and in what order, and spaces the approaches out so that no account is contacted twice in the same period. Use it when running `ref/mkt/account-based-play`.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Contact coordination

## What it does

Settles who approaches which account and in what order, and spaces the
approaches out so that no account is contacted twice in the same period.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Agree the Split with Sales**
  - `ref/mkt/account-based-play`, activity 4 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Keep the Touches in Step**
  - `ref/mkt/account-based-play`, activity 15 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
