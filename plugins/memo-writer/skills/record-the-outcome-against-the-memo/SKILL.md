---
name: record-the-outcome-against-the-memo
description: Records a pass or a decline with its reason and what would bring the deal back. Use it when running `ref/pc/decide-at-investment-committee`, `ref/pc/write-off-a-failed-investment` and `ref/pc/write-the-investment-memo`.
license: CC-BY-4.0
metadata:
  agent: memo-writer
  agent-version: "1"
---

# Record the outcome against the memo

## What it does

Records a pass or a decline with its reason and what would bring the
deal back. For a failed holding it marks each claim in the approved memo
held, failed or never tested, and writes the lessons where the next
memo's author will read them.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **File the Write-Off Record**
  - `ref/pc/write-off-a-failed-investment`, activity 17 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Read the Memo against What Happened**
  - `ref/pc/write-off-a-failed-investment`, activity 14 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)
- **Record a Decline with Its Reason**
  - `ref/pc/decide-at-investment-committee`, activity 16 -
    [Decide at Investment Committee](../../../../processes/private-capital/decide-at-investment-committee.md)
- **Record a Pass**
  - `ref/pc/write-the-investment-memo`, activity 17 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Lessons**
  - `ref/pc/write-off-a-failed-investment`, activity 15 -
    [Write Off a Failed Investment](../../../../processes/private-capital/write-off-a-failed-investment.md)

## What to record

Each memo is kept at every version in the version log, with the date it
was written, what changed from the version before, and which version the
committee read. Every claim in a version carries a link to the finding,
the model case or the source under it, or a mark saying it is the deal
team's view, and the memo names the model version and the mandate result
version it rests on. Each risk is written with how likely it is, what it
would cost and what handles it, and a risk that nothing handles is
written as accepted with the name of the person who accepts it. Each
open question says what would settle it and whether settling it is a
condition of the investment. The challenge partner's points are kept in
the challenger's words, each with its answer or marked open. The run
records which version the deal lead signed and when it reached the
committee against the reading deadline, and each written answer to a
member's question is tied to a finding or marked open. A pass or a
decline is recorded with its reason, the findings behind it and what
would have to change for the firm to look again. For a failed holding,
each claim in the memo as the committee approved it is marked held,
failed or never tested, and the lessons are filed beside the write-off
record. An auditor can take any sentence in a memo the committee read
and find the evidence it rested on at the date it was written.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
