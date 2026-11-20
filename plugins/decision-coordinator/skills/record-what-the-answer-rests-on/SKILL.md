---
name: record-what-the-answer-rests-on
description: Writes down what the answer rests on and what would reopen it, including the assumptions, the figures behind a change, and the date the answer gets looked at again. Use it when running `ref/fin/approve-an-investment-case` and 16 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Record what the answer rests on

## What it does

Writes down what the answer rests on and what would reopen it, including
the assumptions, the figures behind a change, and the date the answer
gets looked at again.

## Where it happens

The agent does this in nine activities across seventeen reference
processes. Each one names the activity as that process words it.

- **Record What the Budget Rests On**
  - `ref/mkt/set-marketing-budget`, activity 15 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Record What the Plan Rests On**
  - `ref/mkt/annual-marketing-plan`, activity 16 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/content-calendar`, activity 15 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Record What the Review Rests On**
  - `ref/mkt/quarterly-business-review`, activity 16 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Record What the Round Rests On**
  - `ref/mkt/prioritize-initiatives`, activity 16 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Record Why the Money Moved**
  - `ref/mkt/reallocate-media-spend`, activity 14 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)
- **Set When the Case Is Read Again**
  - `ref/fin/approve-an-investment-case`, activity 17 -
    [Approve an Investment Case](../../../../processes/finance/approve-an-investment-case.md)
- **Set When the Plan Is Read Again**
  - `ref/hr/plan-the-workforce`, activity 16 -
    [Plan the Workforce](../../../../processes/human-resources/plan-the-workforce.md)
- **Set the Next Review**
  - `ref/hr/plan-succession-for-key-roles`, activity 14 -
    [Plan Succession for Key Roles](../../../../processes/human-resources/plan-succession-for-key-roles.md)
- **Set the Review Conditions**
  - `ref/mkt/attribution-model`, activity 15 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
  - `ref/mkt/develop-marketing-strategy`, activity 16 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
  - `ref/mkt/ideal-customer-profile`, activity 16 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
  - `ref/mkt/lead-scoring-model`, activity 17 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
  - `ref/mkt/map-buyer-journey`, activity 18 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
  - `ref/mkt/product-positioning`, activity 16 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
  - `ref/mkt/segment-the-market`, activity 17 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
  - `ref/mkt/size-market-opportunity`, activity 15 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)

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
