---
name: check-a-claim-against-its-approval
description: "Checks the claim one question at a time, each pass leaving its own finding: every document present, the activity the same one that was approved on date, place and scope, each cost eligible, the invoices real, and nothing claimed a second time somewhere else. Use it when running `ref/prt/check-and-pay-a-claim`."
license: CC-BY-4.0
metadata:
  agent: claim-check
  agent-version: "1"
---

# Check a claim against its approval

## What it does

Checks the claim one question at a time, each pass leaving its own
finding: every document present, the activity the same one that was
approved on date, place and scope, each cost eligible, the invoices
real, and nothing claimed a second time somewhere else.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Check Each Cost Is Eligible**
  - `ref/prt/check-and-pay-a-claim`, activity 5 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Check Nothing Is Claimed Twice**
  - `ref/prt/check-and-pay-a-claim`, activity 8 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Check the Claim Is Complete**
  - `ref/prt/check-and-pay-a-claim`, activity 2 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Check the Evidence of the Activity**
  - `ref/prt/check-and-pay-a-claim`, activity 4 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Check the Invoices**
  - `ref/prt/check-and-pay-a-claim`, activity 6 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)
- **Match the Claim to Its Approval**
  - `ref/prt/check-and-pay-a-claim`, activity 3 -
    [Check and Pay a Claim](../../../../processes/partners/check-and-pay-a-claim.md)

## What to record

Per claim: the approval it was checked against, at its version, and the
evidence list agreed at that approval. The completeness check, naming
every document the approval asked for and whether it arrived. The match
between the activity claimed and the activity approved, on date, place
and scope. Each evidence item marked present, missing or insufficient.
Each cost line scored against the eligible activity list at its version,
with the rule it passes or fails. The invoice check, naming amounts,
dates, tax treatment and who was actually paid. The duplicate check,
naming where else a cost appeared if it did. The score, with the amount
payable, the amount cut, and a reason on every cut. For any line the
rules could not reach, the person who decided it and what they decided.
A run can be replayed line by line from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
