---
name: test-a-claim-against-the-rules
description: Looks for a claim already live on the same customer, applies the published rules in order and marks each one passed or failed with the reason, and carries the result to the named person who approves, declines or holds it. Use it when running `ref/prt/register-a-deal`.
license: CC-BY-4.0
metadata:
  agent: deal-registration-keeper
  agent-version: "1"
---

# Test a claim against the rules

## What it does

Looks for a claim already live on the same customer, applies the
published rules in order and marks each one passed or failed with the
reason, and carries the result to the named person who approves,
declines or holds it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check for an Existing Claim**
  - `ref/prt/register-a-deal`, activity 4 -
    [Register a Deal](../../../../processes/partners/register-a-deal.md)
- **Decide the Registration**
  - `ref/prt/register-a-deal`, activity 9 -
    [Register a Deal](../../../../processes/partners/register-a-deal.md)
- **Test It Against the Rules**
  - `ref/prt/register-a-deal`, activity 6 -
    [Register a Deal](../../../../processes/partners/register-a-deal.md)

## What to record

The submission as it arrived, and the single account record it resolved
to. Every published rule applied in order, each marked passed or failed
with the reason, and the rule set at the version that was applied. What
the partner brought, marked evidenced, asserted or absent. The answer,
the person who gave it, and the rule or the gap they gave as the reason.
What the approval covers and what it does not, written so a deal outside
it can be recognized as outside it. The start and end dates, with the
clause in the agreement they came from. What has moved on the deal, read
from the CRM rather than from what the partner reports. The warning, its
date, and anything the partner said in reply. The close as converted,
extended or expired, with the reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
