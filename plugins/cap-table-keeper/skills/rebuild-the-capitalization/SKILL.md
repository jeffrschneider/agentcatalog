---
name: rebuild-the-capitalization
description: Rebuilds every share, option, warrant and convertible from the company's own records, checks each issue was approved, paid for and recorded, and reads the rights and incentive plans behind every share. Use it when running `ref/pc/run-legal-and-compliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: cap-table-keeper
  agent-version: "1"
---

# Rebuild the capitalization

## What it does

Rebuilds every share, option, warrant and convertible from the company's
own records, checks each issue was approved, paid for and recorded, and
reads the rights and incentive plans behind every share. It hands the
rebuilt table and its gaps on as findings.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Check the Share History**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 7 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Hand the Findings On**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 19 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Read Employment and Incentive Plans**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 13 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Read the Shareholder Rights**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 8 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Rebuild the Capitalization**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 6 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)

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
