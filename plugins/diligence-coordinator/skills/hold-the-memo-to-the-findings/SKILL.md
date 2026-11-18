---
name: hold-the-memo-to-the-findings
description: Takes the rated findings and the issued model into the memo, lists any request still open and any finding still unrated, and works with the memo-writer agent so each strand of diligence is written up with its rating and each risk with what handles it. Use it when running `ref/pc/write-the-investment-memo`.
license: CC-BY-4.0
metadata:
  agent: diligence-coordinator
  agent-version: "1"
---

# Hold the memo to the findings

## What it does

Takes the rated findings and the issued model into the memo, lists any
request still open and any finding still unrated, and works with the
memo-writer agent so each strand of diligence is written up with its
rating and each risk with what handles it. It links every claim in the
memo to the finding under it, and a claim with nothing under it is cut
or marked as the deal team's view.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Check Nothing Is Still Open**
  - `ref/pc/write-the-investment-memo`, activity 2 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Take in the Findings and the Model**
  - `ref/pc/write-the-investment-memo`, activity 1 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Tie Every Claim to Its Evidence**
  - `ref/pc/write-the-investment-memo`, activity 10 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write Up the Findings**
  - `ref/pc/write-the-investment-memo`, activity 6 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)
- **Write the Risks and What Handles Them**
  - `ref/pc/write-the-investment-memo`, activity 7 -
    [Write the Investment Memo](../../../../processes/private-capital/write-the-investment-memo.md)

## What to record

The thesis at its version, with every claim it assumes written out as a
thing to be proved. What was in scope and what was cut, named as cut.
The access agreement, saying who gives what, to whom, and by when. The
numbered request log: each request, who it went to, when it was
answered, and what the answer was. The financial reading, naming
revenue, runway and how concentrated the revenue is. The ownership
finding on anything the company would embed or resell. Every finding
rated on the scale in force, with an owner and a date. Every claim that
stayed unproved, named as unproved rather than dropped. The report to
the sponsor, naming go, go with conditions or stop, and listing every
area that was cut from scope.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
