---
name: write-up-and-defend-the-mark
description: "Writes one file per holding and puts it in front of each reviewer in turn: the outside adviser, the chief financial officer (CFO), the valuation committee and, at year end, the auditor. Use it when running `ref/pc/close-the-year-end-audit-and-tax-documents` and `ref/pc/value-the-portfolio`."
license: CC-BY-4.0
metadata:
  agent: valuation-analyst
  agent-version: "1"
---

# Write up and defend the mark

## What it does

Writes one file per holding and puts it in front of each reviewer in
turn: the outside adviser, the chief financial officer (CFO), the
valuation committee and, at year end, the auditor. A mark that moves
comes back as a new version for the committee to approve.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Approve Any Change to a Mark**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 9 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Get an Outside View of Named Holdings**
  - `ref/pc/value-the-portfolio`, activity 10 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Present the Marks to the Committee**
  - `ref/pc/value-the-portfolio`, activity 13 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Review the Marks as CFO**
  - `ref/pc/value-the-portfolio`, activity 12 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)
- **Support the Valuations under Test**
  - `ref/pc/close-the-year-end-audit-and-tax-documents`, activity 5 -
    [Close the Year-End Audit and Tax Documents](../../../../processes/private-capital/close-the-year-end-audit-and-tax-documents.md)
- **Write Up Each Mark**
  - `ref/pc/value-the-portfolio`, activity 9 -
    [Value the Portfolio](../../../../processes/private-capital/value-the-portfolio.md)

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
