---
name: keep-the-two-sides-in-step
description: Logs every approach on the day it was made, holds the touches that would put the customer in front of both sides at once, and runs the joint check-in against the one plan with each step marked done, open or dropped. Use it when running `ref/prt/run-a-co-sell`.
license: CC-BY-4.0
metadata:
  agent: co-sell-coordinator
  agent-version: "1"
---

# Keep the two sides in step

## What it does

Logs every approach on the day it was made, holds the touches that would
put the customer in front of both sides at once, and runs the joint
check-in against the one plan with each step marked done, open or
dropped.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hold the Joint Check-In**
  - `ref/prt/run-a-co-sell`, activity 14 -
    [Run a Co-Sell](../../../../processes/partners/run-a-co-sell.md)
- **Keep the Approaches in Step**
  - `ref/prt/run-a-co-sell`, activity 13 -
    [Run a Co-Sell](../../../../processes/partners/run-a-co-sell.md)

## What to record

The pursuit as taken in, and what each side said the other brings. The
lead named in writing, who decided it, and the rule they decided it
under. The named people on both sides with what each is there to do, and
the division of the solution written so a question can be routed to a
side without asking. The one plan, every step with a date and a named
owner, at a version, with each earlier version kept so a change can be
read later. The contact rule with the waiting period. The briefing, and
who on each side heard it. Every approach as it actually happened,
logged by the side that made it on the day it was made, and every touch
that was held with the reason. The check-in with each step marked done,
open or dropped. Which side papered it, on what terms, what the other
side invoices, and the debrief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
