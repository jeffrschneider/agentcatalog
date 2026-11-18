---
name: open-the-close
description: Takes in the close date, whether it is the first, a later or the final close, the investors joining and the commitment each has stated, and starts the clock that runs to the signing. Use it when running `ref/pc/hold-a-fund-close`.
license: CC-BY-4.0
metadata:
  agent: subscription-reviewer
  agent-version: "1"
---

# Open the close

## What it does

Takes in the close date, whether it is the first, a later or the final
close, the investors joining and the commitment each has stated, and
starts the clock that runs to the signing.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Take in the Close**
  - `ref/pc/hold-a-fund-close`, activity 1 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)

## What to record

The close as taken in: its date, whether it is the first, a later or the
final close, the investors joining and the commitment each stated. Per
investor: the completeness check naming every page, form, signature and
tax form, and the commitment on the documents set beside the commitment
stated; the one list of missing items sent, with its date and the date
the items arrived or did not; the eligibility finding naming the
offering rule the investor qualifies under, its tax position, any
benefit plan status and the evidence of the signer's authority; the
screening result as read, with the chief compliance officer's clearance
of any hit; and the acceptance as the GP gave it, in whole, in part with
the cut and the allocation rule it came from, or a refusal with its
reason in the terms of the offering rules. The close clock with each
warning raised and to whom. The filed close record, with the signed
documents, the investor register, the screening results and the
acceptances. Any admitted investor can be traced from its stated
commitment to its signed acceptance and the evidence that it was
eligible.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
