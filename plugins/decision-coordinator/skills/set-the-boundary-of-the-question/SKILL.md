---
name: set-the-boundary-of-the-question
description: Says what is inside the question and what sits outside it, which covers where the market ends, what the round or the review takes in, the date it has to decide by, and what a buyer would pick instead. Use it when running `ref/mkt/prioritize-initiatives` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Set the boundary of the question

## What it does

Says what is inside the question and what sits outside it, which covers
where the market ends, what the round or the review takes in, the date
it has to decide by, and what a buyer would pick instead.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Draw the Market Boundary**
  - `ref/mkt/size-market-opportunity`, activity 2 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Name the Competing Choices**
  - `ref/mkt/product-positioning`, activity 7 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Open the Round**
  - `ref/mkt/prioritize-initiatives`, activity 1 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Set What the Review Covers**
  - `ref/mkt/quarterly-business-review`, activity 1 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Set the Market Boundary**
  - `ref/mkt/segment-the-market`, activity 2 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)

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
