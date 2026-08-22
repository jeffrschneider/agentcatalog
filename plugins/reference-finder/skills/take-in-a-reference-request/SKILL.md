---
name: take-in-a-reference-request
description: "Reads the request that starts a run: who is asking and what the deal turns on. Use it when running `ref/sls/provide-a-reference`."
license: CC-BY-4.0
metadata:
  agent: reference-finder
  agent-version: "1"
---

# Take in a reference request

## What it does

Reads the request that starts a run: who is asking and what the deal
turns on. What the prospect actually has to hear is written down before
anybody is searched for, in terms of the industry, the size, the
deployment shape and the specific worry.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Say What the Prospect Must Hear**
  - `ref/sls/provide-a-reference`, activity 2 -
    [Provide a Reference](../../../../processes/sales/provide-a-reference.md)
- **Take in the Reference Request**
  - `ref/sls/provide-a-reference`, activity 1 -
    [Provide a Reference](../../../../processes/sales/provide-a-reference.md)

## What to record

What the prospect must hear, written down before the search: the
industry, the size, the deployment shape and the specific worry. The
candidates found, each with the match reason and the date their written
agreement was last current. Each candidate's last ask date and count for
the period. The health check and what it ruled out. The ranked
shortlist, with a reason per name. The ask, who made it, and the answer,
with a no recorded as a no and no reason demanded. The agreed bounds on
numbers, names, terms and dates. Both briefings. The confirmed time and
how both sides joined. The thanks, timed, written against the customer's
record. The reset clock, naming the date the customer comes back on the
available list and the count for the period.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
