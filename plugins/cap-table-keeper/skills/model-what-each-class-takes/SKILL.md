---
name: model-what-each-class-takes
description: Models the fund's fully diluted ownership and runs a value through the debt, the preferences, conversion and participation to each share class, whether that value is an exit case, a quarter's mark, a buyer's final bid or what is left of a failed company. Use it when running `ref/pc/build-the-investment-model` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: cap-table-keeper
  agent-version: "1"
---

# Model what each class takes

## What it does

Models the fund's fully diluted ownership and runs a value through the
debt, the preferences, conversion and participation to each share class,
whether that value is an exit case, a quarter's mark, a buyer's final
bid or what is left of a failed company.

## Where it happens

The agent does this in six activities across four reference processes.
Each one names the activity as that process words it.

- **Allocate Value across the Share Classes**
  - `ref/pc/value-the-portfolio`, activity 8 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Compare the Final Bids**
  - `ref/pc/run-a-sale-process`, activity 11 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)
- **Confirm Nothing Is Left for the Fund**
  - `ref/pc/write-off-a-failed-investment`, activity 2 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Hand the Model On**
  - `ref/pc/build-the-investment-model`, activity 17 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)
- **Model the Ownership**
  - `ref/pc/build-the-investment-model`, activity 4 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)
- **Model the Preferences**
  - `ref/pc/build-the-investment-model`, activity 5 -
    [Build the Investment Model](../../../../processes/private-capital/build-the-investment-model.md)

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
