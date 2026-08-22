---
name: answer-what-the-registration-record-holds
description: Answers another run that needs to know who holds what. Use it when running `ref/prt/resolve-a-channel-conflict` and `ref/prt/run-a-co-sell`.
license: CC-BY-4.0
metadata:
  agent: deal-registration-keeper
  agent-version: "1"
---

# Answer what the registration record holds

## What it does

Answers another run that needs to know who holds what. Pulls what each
side holds on a contested customer, establishes which claim came first,
and confirms the claim and the terms covering a deal about to be worked
jointly.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Claim and the Terms**
  - `ref/prt/run-a-co-sell`, activity 2 -
    [Run a Co-Sell](../../../../processes/partners/run-a-co-sell.md)
- **Establish Who Was First**
  - `ref/prt/resolve-a-channel-conflict`, activity 6 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)
- **Pull What Each Side Holds**
  - `ref/prt/resolve-a-channel-conflict`, activity 4 -
    [Resolve a Channel Conflict](../../../../processes/partners/resolve-a-channel-conflict.md)

## What to record

The submission as it arrived, and the single account record it resolved
to. Every published rule applied in order, each marked passed or failed
with the reason, and the rule set at the version that was applied. What
the partner brought, marked evidenced, asserted or absent. The answer,
the person who gave it, and the rule or the gap they gave as the reason.
What the approval covers and what it does not, written so a deal outside
it can be recognized as outside it. The start and end dates, with the
clause in the agreement they came from. What has moved on the deal, read
from the CRM rather than from what the partner reports. The warning, its
date, and anything the partner said in reply. The close as converted,
extended or expired, with the reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
