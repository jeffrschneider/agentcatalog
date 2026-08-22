---
name: classify-every-change
description: Marks each change as standard language, an approved fallback, or new text nobody has agreed to before, and reads it against what was decided the last time the same change came up. Use it when running `ref/sls/review-the-redlines`.
license: CC-BY-4.0
metadata:
  agent: redline-reviewer
  agent-version: "1"
---

# Classify every change

## What it does

Marks each change as standard language, an approved fallback, or new
text nobody has agreed to before, and reads it against what was decided
the last time the same change came up. The liability, indemnity and data
terms are read with a lawyer.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check Against Prior Decisions**
  - `ref/sls/review-the-redlines`, activity 5 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Classify Each Change**
  - `ref/sls/review-the-redlines`, activity 4 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Review the Risk Terms**
  - `ref/sls/review-the-redlines`, activity 7 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)

## What to record

Per review: the markup at its version and the copy it was made from. One
item per changed clause, with the original text and the buyer's text
side by side, its class, and its clause number. What was decided on the
same change in past deals and who decided it. Every clause closed as
accept, counter or reject, each with its reason and the person who made
the decision. The counter-markup with every off-template term listed
separately and every approver named. The version sent back and the date.
Each further markup read against the copy we last sent, with every
difference named. The confirmed clean text, and the accepted changes
written to the record other deals read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
