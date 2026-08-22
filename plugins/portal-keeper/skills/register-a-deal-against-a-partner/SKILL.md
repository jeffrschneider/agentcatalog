---
name: register-a-deal-against-a-partner
description: Registers a deal against the partner with its protection period, so the same deal cannot be worked twice or claimed later. Use it when running `ref/prt/run-a-first-deal-together`.
license: CC-BY-4.0
metadata:
  agent: portal-keeper
  agent-version: "1"
---

# Register a deal against a partner

## What it does

Registers a deal against the partner with its protection period, so the
same deal cannot be worked twice or claimed later.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Register the Deal**
  - `ref/prt/run-a-first-deal-together`, activity 4 -
    [Run a First Deal Together](../../../../processes/partners/run-a-first-deal-together.md)

## What to record

For every account: the person it belongs to, how they can be reached,
the date it was opened and who asked for it. For everything switched on
or left off: the tier rule or the agreement clause that decided it. For
every material published: the version and the date it went to the
partner. The end-to-end test that proved a path works, because no access
is counted as granted until something the partner raised arrived where
it should. For every registered deal: the partner, the date and the
protection period. For every closure: the date, the reason and who told
us.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
