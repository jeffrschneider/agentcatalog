---
name: place-people-against-the-decisions
description: Places each person against a named decision rather than against the logo, and says whether they decide, influence, block or use. Use it when running `ref/pc/reach-out-to-a-company` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: relationship-mapper
  agent-version: "1"
---

# Place people against the decisions

## What it does

Places each person against a named decision rather than against the
logo, and says whether they decide, influence, block or use. Reads the
reporting lines behind any claim of authority, and names the buyer
behind an opportunity a plan carries.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Find Who Decides at the Company**
  - `ref/pc/reach-out-to-a-company`, activity 4 -
    [Reach Out to a Company](../../../../processes/private-capital/reach-out-to-a-company.md)
- **Map the Investor's Decision**
  - `ref/pc/work-an-investor-prospect`, activity 6 -
    [Work an Investor Prospect](../../../../processes/private-capital/work-an-investor-prospect.md)
- **Name Who Buys Each One**
  - `ref/sls/write-an-account-plan`, activity 7 -
    [Write an Account Plan](../../../../processes/sales/write-an-account-plan.md)
- **Place People Against a Decision**
  - `ref/sls/map-the-account-people`, activity 5 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)
- **Read the Reporting Lines**
  - `ref/sls/map-the-account-people`, activity 6 -
    [Map the People at an Account](../../../../processes/sales/map-the-account-people.md)

## What to record

Per person: the decision they sit under, whether they decide, influence,
block or use, the source they were found in and that source's
publication date, the reporting line behind any claim of authority, the
strength score with the contact history it was computed from, the path
in and who at our end holds it, and the stance with what was said or
done behind it. Per map: every decision with no decider found or nobody
we know marked as a gap rather than left blank, what the privacy check
removed and the rule behind each removal, and the issued version naming
who corrected what and when they signed. A claim that somebody knows a
buyer well is recorded as a claim, with the person who made it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
