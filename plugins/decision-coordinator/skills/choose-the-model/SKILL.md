---
name: choose-the-model
description: One model chosen, with the reasons written down. Use it when running `ref/mkt/attribution-model` and `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Choose the Model

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/attribution-model`, one model chosen, with the reasons
  written down
- in `ref/mkt/lead-scoring-model`, one candidate chosen, with the
  reasons said out loud

## Where it happens

- `ref/mkt/attribution-model`, activity 10 -
  [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- `ref/mkt/lead-scoring-model`, activity 11 -
  [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

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
