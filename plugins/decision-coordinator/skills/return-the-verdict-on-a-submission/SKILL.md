---
name: return-the-verdict-on-a-submission
description: Pulls every finding into one list with the rule each one broke, sends the failures back to whoever submitted them, records in writing any failure that is knowingly accepted and the reasons for it, and releases the cleared version to the requester. Use it when running `ref/mkt/approve-marketing-material`.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Return the verdict on a submission

## What it does

Pulls every finding into one list with the rule each one broke, sends
the failures back to whoever submitted them, records in writing any
failure that is knowingly accepted and the reasons for it, and releases
the cleared version to the requester.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Gather the Findings into One List**
  - `ref/mkt/approve-marketing-material`, activity 9 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Record an Accepted Exception**
  - `ref/mkt/approve-marketing-material`, activity 11 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Release the Cleared Version**
  - `ref/mkt/approve-marketing-material`, activity 13 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Return the Failures to the Submitter**
  - `ref/mkt/approve-marketing-material`, activity 10 -
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
