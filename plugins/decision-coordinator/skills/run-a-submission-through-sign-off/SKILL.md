---
name: run-a-submission-through-sign-off
description: Records what was submitted and at which version, checks that the material, its claims and its sources are all there, names which standards apply and who has to sign, and gets those signatures against that one version. Use it when running `ref/mkt/approve-marketing-material`.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Run a submission through sign off

## What it does

Records what was submitted and at which version, checks that the
material, its claims and its sources are all there, names which
standards apply and who has to sign, and gets those signatures against
that one version.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Submission Is Complete**
  - `ref/mkt/approve-marketing-material`, activity 3 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Get the Signatures**
  - `ref/mkt/approve-marketing-material`, activity 12 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Name the Standards and the Signers**
  - `ref/mkt/approve-marketing-material`, activity 2 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Take in the Submission**
  - `ref/mkt/approve-marketing-material`, activity 1 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)

## What to record

The decision written down as a question before any evidence is gathered:
what it has to settle, who decides it, what evidence it needs and from
which agent, and the date it is due. The evidence as it came in, each
line attributed to the agent and the source behind it. The candidate
answers, each written out with what it would cost and what it would rule
out. The answer at a version, naming who decided it, on what date, for
what reasons, and anyone who disagreed with what that person said. A
handover line for each agent that has to act on the answer, naming the
agent and what it was given. The review date, set at the moment the
answer is recorded.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
