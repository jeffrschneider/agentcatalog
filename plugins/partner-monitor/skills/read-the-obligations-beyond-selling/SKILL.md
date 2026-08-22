---
name: read-the-obligations-beyond-selling
description: "Reads what a partner owes besides revenue, in the same round as the numbers: the certifications held and by whom, the marketing run, the support given and the reporting delivered. Use it when running `ref/prt/certify-a-partner` and `ref/prt/review-partner-performance`."
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Read the obligations beyond selling

## What it does

Reads what a partner owes besides revenue, in the same round as the
numbers: the certifications held and by whom, the marketing run, the
support given and the reporting delivered. Certificates lapse and
certified people leave, so it keeps a dated line for each.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check What They Already Know**
  - `ref/prt/certify-a-partner`, activity 3 -
    [Certify a Partner](../../../../processes/partners/certify-a-partner.md)
- **Read the Obligations Beyond Selling**
  - `ref/prt/review-partner-performance`, activity 5 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)
- **Watch for Expiry and Drift**
  - `ref/prt/certify-a-partner`, activity 16 -
    [Certify a Partner](../../../../processes/partners/certify-a-partner.md)

## What to record

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
