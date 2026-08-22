---
name: record-the-choice-that-was-made
description: Takes the answer the named deciders picked and writes it down with the reasons they gave and the names of anyone who disagreed. Use it when running `ref/mkt/annual-marketing-plan` and 21 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Record the choice that was made

## What it does

Takes the answer the named deciders picked and writes it down with the
reasons they gave and the names of anyone who disagreed. This agent
picks none of it itself, which is what makes the record worth trusting
later.

## Where it happens

The agent does this in 25 activities across 22 reference processes. Each
one names the activity as that process words it.

- **Agree Who the Company Is For**
  - `ref/mkt/brand-positioning`, activity 5 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
- **Agree the Calendar**
  - `ref/mkt/content-calendar`, activity 11 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Choose What Gets Committed**
  - `ref/mkt/prioritize-initiatives`, activity 10 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Choose Where to Play and How to Win**
  - `ref/mkt/develop-marketing-strategy`, activity 10 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Choose the Agency**
  - `ref/mkt/engage-marketing-agency`, activity 12 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Choose the Identity**
  - `ref/mkt/brand-identity`, activity 9 -
    [Develop Brand Identity](../../../../processes/marketing/brand-identity.md)
- **Choose the Initiatives**
  - `ref/mkt/annual-marketing-plan`, activity 9 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
- **Choose the Mix**
  - `ref/mkt/media-plan`, activity 8 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Choose the Model**
  - `ref/mkt/attribution-model`, activity 10 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
  - `ref/mkt/lead-scoring-model`, activity 11 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Choose the Name**
  - `ref/mkt/name-product`, activity 12 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Choose the Position**
  - `ref/mkt/brand-positioning`, activity 9 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
  - `ref/mkt/product-positioning`, activity 11 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Choose the Route**
  - `ref/mkt/engage-marketing-agency`, activity 2 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Choose the Tool**
  - `ref/mkt/select-marketing-technology`, activity 17 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Decide What Happens to Each Surface**
  - `ref/mkt/brand-refresh`, activity 8 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Decide What Happens to Published Reports**
  - `ref/mkt/attribution-model`, activity 11 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Decide What Is Handed Over**
  - `ref/mkt/engage-marketing-agency`, activity 3 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Decide the Mix**
  - `ref/mkt/plan-marketing-capacity`, activity 11 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Reset the Commitments**
  - `ref/mkt/quarterly-business-review`, activity 11 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Set the Switch Date and the Order**
  - `ref/mkt/brand-refresh`, activity 10 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Settle What May Be Said**
  - `ref/mkt/competitive-battlecard`, activity 6 -
    [Refresh Competitive Battlecard](../../../../processes/marketing/competitive-battlecard.md)
- **Settle on One Division**
  - `ref/mkt/segment-the-market`, activity 12 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Settle on One Profile**
  - `ref/mkt/ideal-customer-profile`, activity 12 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Settle on the Number**
  - `ref/mkt/size-market-opportunity`, activity 12 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)
- **Settle the Map**
  - `ref/mkt/map-buyer-journey`, activity 14 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Settle the Tiers and the Terms**
  - `ref/mkt/channel-program`, activity 2 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)

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
