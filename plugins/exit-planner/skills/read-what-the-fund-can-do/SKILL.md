---
name: read-what-the-fund-can-do
description: Writes down the reason to exit and reads what the fund holds and can force, the fund's term and its extensions, and, after a listing, the lock-up, the trading windows, the holder limits and the filings each sale triggers. Use it when running `ref/pc/plan-the-exit` and `ref/pc/sell-down-a-public-position`.
license: CC-BY-4.0
metadata:
  agent: exit-planner
  agent-version: "1"
---

# Read what the fund can do

## What it does

Writes down the reason to exit and reads what the fund holds and can
force, the fund's term and its extensions, and, after a listing, the
lock-up, the trading windows, the holder limits and the filings each
sale triggers.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Read What the Fund Holds and Can Force**
  - `ref/pc/plan-the-exit`, activity 2 -
    [Plan the Exit](../../../../processes/private-capital/plan-the-exit.md)
- **Read the Fund's Term and Timing**
  - `ref/pc/plan-the-exit`, activity 3 -
    [Plan the Exit](../../../../processes/private-capital/plan-the-exit.md)
- **Read the Lock-Up and the Holder Rules**
  - `ref/pc/sell-down-a-public-position`, activity 2 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Take in the Reason to Exit**
  - `ref/pc/plan-the-exit`, activity 1 -
    [Plan the Exit](../../../../processes/private-capital/plan-the-exit.md)

## What to record

An exit plan leaves the reason to exit with its date and who raised it,
the fund's rights read from the shareholders' agreement, the fund's end
date and the extensions it allows, every route with what it needs from
the other shareholders, the likely buyers with why each would pay and
any the fund will not sell to, the issues that would lower the price
with what each would cost, and the preparation work with an owner and a
date on each item. Management's terms for the exit are written down with
the date they were disclosed to the board and the committee. The exit
paper is kept at each version, and the approved plan is handed on with
its floor, its conditions and its buyers. A sale leaves the company's
information checked against its records, the data room index with each
buyer's access and every view, the reason each buyer was kept or let go,
a diligence log of every question with its answer, its date and whether
it went to every buyer, and each condition to close with its owner and
its date. A sell-down leaves the lock-up's end date, the trading windows
and the holder limits, the broker chosen with its price, reach and fee,
each execution matched to its signed instruction, every filing with the
date it was made beside its deadline, and the shares left with the next
window. Each result is recorded against the plan, with the price and the
return, every amount held back with its release date, and what the exit
taught.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
