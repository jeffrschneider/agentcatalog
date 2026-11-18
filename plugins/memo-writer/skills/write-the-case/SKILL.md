---
name: write-the-case
description: Writes the thesis as the claims diligence tested, each strand of findings with its rating and the areas cut from scope, each risk with what handles it, the returns from the issued model at its version, and the proposed terms inside the mandate result. Use it when running `ref/pc/write-the-investment-memo`.
license: CC-BY-4.0
metadata:
  agent: memo-writer
  agent-version: "1"
---

# Write the case

## What it does

Writes the thesis as the claims diligence tested, each strand of
findings with its rating and the areas cut from scope, each risk with
what handles it, the returns from the issued model at its version, and
the proposed terms inside the mandate result.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Write Up the Findings**
  - `ref/pc/write-the-investment-memo`, activity 6 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Proposed Terms**
  - `ref/pc/write-the-investment-memo`, activity 9 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Returns**
  - `ref/pc/write-the-investment-memo`, activity 8 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Risks and What Handles Them**
  - `ref/pc/write-the-investment-memo`, activity 7 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Thesis**
  - `ref/pc/write-the-investment-memo`, activity 5 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)

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
