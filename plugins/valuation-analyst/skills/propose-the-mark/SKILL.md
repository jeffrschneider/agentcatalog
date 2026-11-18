---
name: propose-the-mark
description: Chooses the method the policy sets for each holding, calibrates it to the last price, and proposes the company's value with every input and judgment written down. Use it when running `ref/pc/value-the-portfolio` and `ref/pc/write-off-a-failed-investment`.
license: CC-BY-4.0
metadata:
  agent: valuation-analyst
  agent-version: "1"
---

# Propose the mark

## What it does

Chooses the method the policy sets for each holding, calibrates it to
the last price, and proposes the company's value with every input and
judgment written down. It runs that value through the share classes with
the cap-table-keeper agent, and proposes a mark at zero when nothing is
left.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Allocate Value across the Share Classes**
  - `ref/pc/value-the-portfolio`, activity 8 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Calibrate to the Last Price**
  - `ref/pc/value-the-portfolio`, activity 6 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Choose the Method for Each Holding**
  - `ref/pc/value-the-portfolio`, activity 5 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Propose the Company's Value**
  - `ref/pc/value-the-portfolio`, activity 7 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Propose the Mark at Zero**
  - `ref/pc/write-off-a-failed-investment`, activity 5 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)

## What to record

Each quarter leaves the measurement date, every holding the fund carried
on it and the policy version in force. Each holding has one file with
the method and the reason for any change from last quarter, the
calibration to the entry or latest round price, every input with its
source and its date, every judgment, the company's value, the allocation
through the preferences to the fund's shares, the proposed mark, and the
change from last quarter explained. A holding whose company did not
report is named as stale in the first line of its file. The outside
adviser's range, the deal lead's view and the CFO's review points sit in
the file beside how each was answered, and the committee pack records
which judgments the committee was asked to test. The approved mark is
kept at the version the committee approved and is tied to that approval
when it is posted, and an event after the measurement date is recorded
on its own. The handoff to the quarterly report gives the marks, their
movements and the plain reason for each, and the debrief compares
earlier marks with the prices later realized. A write-off leaves the
evidence that nothing is left, the zero mark with the last mark it
replaces, the event that realized the loss with its evidence and the tax
adviser's agreement, and a tax file with the fund's cost. At year end it
leaves the support for each tested mark as written at the quarter it was
set, and any moved mark as a new version with its reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
