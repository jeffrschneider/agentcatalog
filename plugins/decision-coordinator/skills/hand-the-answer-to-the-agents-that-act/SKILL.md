---
name: hand-the-answer-to-the-agents-that-act
description: Gives every agent and function that has to act the same account of what was decided, and takes back from each one what it is going to change. Use it when running `ref/fin/approve-an-investment-case` and 24 other reference processes.
license: CC-BY-4.0
metadata:
  agent: decision-coordinator
  agent-version: "1"
---

# Hand the answer to the agents that act

## What it does

Gives every agent and function that has to act the same account of what
was decided, and takes back from each one what it is going to change.
Whoever asked for something hears the answer, including the ones that
were turned down.

## Where it happens

The agent does this in 25 activities across 25 reference processes. Each
one names the activity as that process words it.

- **Announce the Decision**
  - `ref/fin/write-off-a-bad-debt`, activity 12 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)
- **Brief the Department**
  - `ref/mkt/annual-marketing-plan`, activity 15 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/content-calendar`, activity 13 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
  - `ref/mkt/quarterly-business-review`, activity 15 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Brief the Makers**
  - `ref/mkt/brand-voice`, activity 4 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
- **Brief the Managers**
  - `ref/hr/run-the-pay-review`, activity 7 -
    [Run the Pay Review](../../../../processes/human-resources/run-the-pay-review.md)
- **Deliver the Findings**
  - `ref/mkt/customer-research`, activity 19 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Deliver the Themes and Recommendations**
  - `ref/mkt/win-loss-analysis`, activity 20 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Hand On Pay Changes and Ended Roles**
  - `ref/hr/change-the-organization-structure`, activity 12 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **Hand On the Gap the Year Cannot Absorb**
  - `ref/fin/reforecast-the-year`, activity 16 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Hand On the Watch List and Reserves**
  - `ref/pc/run-the-portfolio-review`, activity 17 -
    [Run the Portfolio Review](../../../../processes/private-capital/run-the-portfolio-review.md)
- **Hand On to Formation and Fundraising**
  - `ref/pc/set-the-fund-strategy`, activity 17 -
    [Set the Fund Strategy](../../../../processes/private-capital/set-the-fund-strategy.md)
- **Hand over the Commitments**
  - `ref/mkt/prioritize-initiatives`, activity 15 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Hand over the Map**
  - `ref/mkt/map-buyer-journey`, activity 17 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Hand over the Model**
  - `ref/mkt/lead-scoring-model`, activity 14 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Hand over the Profile**
  - `ref/mkt/ideal-customer-profile`, activity 15 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Hand over the Segments**
  - `ref/mkt/segment-the-market`, activity 16 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Hand the Approved Case On**
  - `ref/fin/approve-an-investment-case`, activity 16 -
    [Approve an Investment Case](../../../../processes/finance/approve-an-investment-case.md)
- **Hand the Approved Terms On**
  - `ref/pc/decide-at-investment-committee`, activity 15 -
    [Decide at Investment Committee](../../../../processes/private-capital/decide-at-investment-committee.md)
- **Hand the Changes to the Record and Payroll**
  - `ref/hr/run-the-pay-review`, activity 16 -
    [Run the Pay Review](../../../../processes/human-resources/run-the-pay-review.md)
- **Hand the Course to the Process That Runs It**
  - `ref/pc/work-a-company-in-trouble`, activity 15 -
    [Work a Company in Trouble](../../../../processes/private-capital/work-a-company-in-trouble.md)
- **Hand the Decisions On**
  - `ref/mkt/brief-executive-leadership`, activity 19 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Hand the Strategy to the Work that Follows**
  - `ref/mkt/develop-marketing-strategy`, activity 15 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Tell Every Function What It Has**
  - `ref/mkt/set-marketing-budget`, activity 14 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Tell the Deal Team**
  - `ref/pc/decide-at-investment-committee`, activity 14 -
    [Decide at Investment Committee](../../../../processes/private-capital/decide-at-investment-committee.md)
- **Tell the Processes that Read It**
  - `ref/mkt/brand-positioning`, activity 15 -
    [Define Brand Positioning](../../../../processes/marketing/brand-positioning.md)
  - `ref/mkt/brand-voice`, activity 16 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
  - `ref/mkt/name-product`, activity 15 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Tell the Requesters**
  - `ref/mkt/prioritize-initiatives`, activity 14 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

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
