---
name: hold-the-terms-to-the-committee-approval
description: Takes in what the investment committee approved, with its conditions and the limits on how far each term may move, and the signed term sheet once there is one. Use it when running `ref/pc/issue-a-term-sheet` and `ref/pc/negotiate-the-definitive-agreements`.
license: CC-BY-4.0
metadata:
  agent: deal-structurer
  agent-version: "1"
---

# Hold the terms to the committee approval

## What it does

Takes in what the investment committee approved, with its conditions and
the limits on how far each term may move, and the signed term sheet once
there is one. It checks every line of a draft against them, and takes a
change past those limits back to the committee with what it does to the
return rather than absorbing it, because only the committee moves its
limits.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Draft Against the Approval**
  - `ref/pc/issue-a-term-sheet`, activity 4 -
    [Issue a Term Sheet](../../../../processes/private-capital/issue-a-term-sheet.md)
- **Take a Change Past the Limits to Committee**
  - `ref/pc/issue-a-term-sheet`, activity 10 -
    [Issue a Term Sheet](../../../../processes/private-capital/issue-a-term-sheet.md)
- **Take a Moved Term Back to Committee**
  - `ref/pc/negotiate-the-definitive-agreements`, activity 11 -
    [Negotiate the Definitive Agreements](../../../../processes/private-capital/negotiate-the-definitive-agreements.md)
- **Take in the Committee Decision**
  - `ref/pc/issue-a-term-sheet`, activity 1 -
    [Issue a Term Sheet](../../../../processes/private-capital/issue-a-term-sheet.md)
- **Take in the Signed Term Sheet**
  - `ref/pc/negotiate-the-definitive-agreements`, activity 1 -
    [Negotiate the Definitive Agreements](../../../../processes/private-capital/negotiate-the-definitive-agreements.md)

## What to record

What each side must get, written before any shape was chosen. The shape
chosen and why it beat the others considered. The money model, naming
who charges the customer, who invoices whom, and who keeps what. The
term and the exit, with the notice each ending needs. The economics at a
version, with the assumptions and the downside case stated. Every
diligence finding, priced into a term or named as a stop. The internal
mandate and its walk-away terms. The term sheet at a version. Every ask
the other side made, the position taken on it, and the date it closed.
Every redline read against the term sheet, saying what moved and who was
told. The obligation register at handover, so the work the agreement
created has owners before anybody starts it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
