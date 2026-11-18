---
name: sell-down-a-listed-position
description: Sets the sell-down plan and the choice between a sale and a distribution with the partners, chooses the broker or the block bank, follows each execution against its signed instruction, files what the rules require, and tracks what is left to sell. Use it when running `ref/pc/sell-down-a-public-position`.
license: CC-BY-4.0
metadata:
  agent: exit-planner
  agent-version: "1"
---

# Sell down a listed position

## What it does

Sets the sell-down plan and the choice between a sale and a distribution
with the partners, chooses the broker or the block bank, follows each
execution against its signed instruction, files what the rules require,
and tracks what is left to sell.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Choose Between a Sale and a Distribution**
  - `ref/pc/sell-down-a-public-position`, activity 4 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Choose the Broker or the Block Bank**
  - `ref/pc/sell-down-a-public-position`, activity 8 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Execute the Sale or the Transfer**
  - `ref/pc/sell-down-a-public-position`, activity 11 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **File What the Rules Require**
  - `ref/pc/sell-down-a-public-position`, activity 12 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Set the Sell-Down Plan**
  - `ref/pc/sell-down-a-public-position`, activity 3 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Track What Is Left to Sell**
  - `ref/pc/sell-down-a-public-position`, activity 15 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)

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
