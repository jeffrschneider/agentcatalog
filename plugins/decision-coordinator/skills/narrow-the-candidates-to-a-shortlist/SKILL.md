---
name: narrow-the-candidates-to-a-shortlist
description: Takes candidates off the list when they break the criteria, and leaves a short list worth spending time and money on. Use it when running `ref/mkt/name-product`.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Narrow the candidates to a shortlist

## What it does

Takes candidates off the list when they break the criteria, and leaves a
short list worth spending time and money on.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Cut to a Shortlist**
  - `ref/mkt/name-product`, activity 8 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Screen the Long List**
  - `ref/mkt/name-product`, activity 5 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)

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
