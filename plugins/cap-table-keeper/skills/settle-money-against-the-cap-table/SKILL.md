---
name: settle-money-against-the-cap-table
description: "Sets the cap table against the money: the funds flow lines at a closing, the payout of a sale holder by holder, and each trade of a sell-down matched to its instruction and confirmation. Use it when running `ref/pc/run-a-sale-process`, `ref/pc/run-the-closing` and `ref/pc/sell-down-a-public-position`."
license: CC-BY-4.0
metadata:
  agent: cap-table-keeper
  agent-version: "1"
---

# Settle money against the cap table

## What it does

Sets the cap table against the money: the funds flow lines at a closing,
the payout of a sale holder by holder, and each trade of a sell-down
matched to its instruction and confirmation. It then hands the proceeds
or the shares on and records the result against the plan.

## Where it happens

The agent does this in six activities across three reference processes.
Each one names the activity as that process words it.

- **Build the Funds Flow**
  - `ref/pc/run-the-closing`, activity 7 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Check the Proceeds against the Cap Table**
  - `ref/pc/run-a-sale-process`, activity 17 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Hand Over the Proceeds or the Shares**
  - `ref/pc/sell-down-a-public-position`, activity 14 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Record the Result**
  - `ref/pc/sell-down-a-public-position`, activity 16 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Record the Result against the Plan**
  - `ref/pc/run-a-sale-process`, activity 19 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Settle and Reconcile Each Sale**
  - `ref/pc/sell-down-a-public-position`, activity 13 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)

## What to record

A diligence run leaves the rebuilt capitalization at a version beside
the table the company supplied, with every share, option, warrant and
convertible traced to the record behind it, every gap named with the
request that would close it, each issue checked for its approval, its
payment and its filing, and each right quoted from its clause. A model
run leaves the fund's ownership before and after the investment, fully
diluted, and a schedule of what each share class takes at each exit
value. A closing leaves the capitalization read line by line against the
agreed text, and the fund's shares, class, price, preferences and rights
written to the cap table record on the closing date with the executed
documents linked. Each quarter leaves the fund's position at the
measurement date and the company's value allocated class by class to the
fund's shares. A sale leaves the payout checked holder by holder and
class by class against the record, with every difference named. A
sell-down leaves each trade settled and matched to its instruction and
the broker's confirmation, and the proceeds or the shares handed to the
distribution with their value and date. A write-off leaves the waterfall
that shows the fund's shares receive nothing, the list of what the fund
still held or owed, and the position closed at zero with the signed
documents attached. An auditor can recompute what the fund's shares
receive at any price from the recorded rights and position.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
