---
name: open-access-for-a-partner
description: Checks the partner record holds enough for access to be opened at all, opens a named login for each person the partner listed, switches on the materials, the prices and the rules that partner's tier allows and leaves everything else off, and opens the systems the agreement covers. Use it when running `ref/prt/onboard-a-partner`.
license: CC-BY-4.0
metadata:
  agent: portal-keeper
  agent-version: "1"
---

# Open access for a partner

## What it does

Checks the partner record holds enough for access to be opened at all,
opens a named login for each person the partner listed, switches on the
materials, the prices and the rules that partner's tier allows and
leaves everything else off, and opens the systems the agreement covers.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Partner Record Is Complete**
  - `ref/prt/onboard-a-partner`, activity 5 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)
- **Create the Portal Accounts**
  - `ref/prt/onboard-a-partner`, activity 6 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)
- **Grant the Systems Access**
  - `ref/prt/onboard-a-partner`, activity 8 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)
- **Set What the Partner Can See**
  - `ref/prt/onboard-a-partner`, activity 7 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)

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
