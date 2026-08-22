---
name: rebuild-the-inventory
description: The agent builds the list of everything the organization has published from what the site and the stores actually serve, recording for each piece what it was made to do, when it last changed and what it is doing now. Use it when running `ref/mkt/annual-marketing-plan` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: content-librarian
  agent-version: "1"
---

# Rebuild the inventory

## What it does

The agent builds the list of everything the organization has published
from what the site and the stores actually serve, recording for each
piece what it was made to do, when it last changed and what it is doing
now.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **List Where the Brand Appears**
  - `ref/mkt/brand-audit`, activity 5 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)
- **Map the Touchpoints**
  - `ref/mkt/map-buyer-journey`, activity 9 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Rebuild the Inventory**
  - `ref/mkt/refresh-content`, activity 2 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Take Stock of What the Department Holds**
  - `ref/mkt/annual-marketing-plan`, activity 3 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
- **Take Stock of the Marks in Use**
  - `ref/mkt/brand-identity`, activity 2 -
    [Develop Brand Identity](../../../../processes/marketing/brand-identity.md)

## What to record

The inventory at a version every time it is rebuilt, with each live page
carrying what it was made to do, the date it last changed, what it is
doing now, and where every figure came from. The refresh cycle's list,
giving the reason each page is on it, and a line for the pages that were
looked at and left for a later cycle. A decision record for every merge,
retirement and redirect, naming the version that came down, what now
stands at its address, and the person who said so. A page it could not
measure is recorded as unmeasured, with the reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
