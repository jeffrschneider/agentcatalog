---
name: hold-the-funds-position
description: "Keeps the fund's position in the cap table record from the closing date to the close at zero: the shares, class, price and rights it bought, its position at each measurement date, its listed shares after a listing, and what it still holds or owes when a company fails. Use it when running `ref/pc/run-the-closing` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: cap-table-keeper
  agent-version: "1"
---

# Hold the funds position

## What it does

Keeps the fund's position in the cap table record from the closing date
to the close at zero: the shares, class, price and rights it bought, its
position at each measurement date, its listed shares after a listing,
and what it still holds or owes when a company fails.

## Where it happens

The agent does this in nine activities across four reference processes.
Each one names the activity as that process words it.

- **Book the Investment**
  - `ref/pc/run-the-closing`, activity 15 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Close the Fund's Position**
  - `ref/pc/write-off-a-failed-investment`, activity 8 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Confirm the Capitalization at Closing**
  - `ref/pc/run-the-closing`, activity 5 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **List What the Fund Still Holds or Owes**
  - `ref/pc/write-off-a-failed-investment`, activity 3 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Make the Shares Ready to Trade**
  - `ref/pc/sell-down-a-public-position`, activity 7 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Read the Fund's Position in Each Company**
  - `ref/pc/value-the-portfolio`, activity 3 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Record the Close in the Cap Table Record**
  - `ref/pc/write-off-a-failed-investment`, activity 11 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Record the Fund's Position**
  - `ref/pc/run-the-closing`, activity 14 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Take in the Listed Position**
  - `ref/pc/sell-down-a-public-position`, activity 1 -
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
