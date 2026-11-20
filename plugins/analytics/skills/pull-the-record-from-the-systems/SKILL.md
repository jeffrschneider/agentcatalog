---
name: pull-the-record-from-the-systems
description: The agent names which systems hold the record for a question, reads them, and returns the figures with the source and the date on every line. Use it when running `ref/hr/plan-the-workforce` and 22 other reference processes.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Pull the record from the systems

## What it does

The agent names which systems hold the record for a question, reads
them, and returns the figures with the source and the date on every
line. A system it could not read appears as missing rather than being
left out.

## Where it happens

The agent does this in 30 activities across 23 reference processes. Each
one names the activity as that process words it.

- **Count the Cases With No Article**
  - `ref/sup/find-gaps-in-the-help-center`, activity 2 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Count the Complaints and Their Outcomes**
  - `ref/sup/report-what-customers-say`, activity 4 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Count the Customers Each Gap Touches**
  - `ref/sup/find-gaps-in-the-help-center`, activity 8 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Gather the Channel Evidence**
  - `ref/mkt/media-plan`, activity 5 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Gather the Evidence**
  - `ref/mkt/award-entry`, activity 6 -
    [Submit Award Entry](../../../../processes/marketing/award-entry.md)
- **Name the Sources**
  - `ref/mkt/analyze-customer-base`, activity 3 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Pull the Cases in the Period**
  - `ref/sup/report-the-service-levels`, activity 4 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Pull the Closed Deals**
  - `ref/mkt/win-loss-analysis`, activity 2 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)
- **Pull the Delivery Quality Figures**
  - `ref/mkt/verify-ad-placement`, activity 5 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Pull the Delivery Record**
  - `ref/mkt/reconcile-media-spend`, activity 3 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Pull the Numbers**
  - `ref/mkt/marketing-performance-report`, activity 3 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Pull the Placement Record**
  - `ref/mkt/verify-ad-placement`, activity 4 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Pull the Record**
  - `ref/mkt/analyze-customer-base`, activity 5 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Pull the Results for the Period**
  - `ref/mkt/brief-executive-leadership`, activity 4 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Pull the Touchpoint Record**
  - `ref/mkt/attribution-model`, activity 4 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Read How Each Article Is Used**
  - `ref/sup/review-the-help-center`, activity 2 -
    [Review the Help Center](../../../../processes/customer-support/review-the-help-center.md)
- **Read Last Year's Spend**
  - `ref/mkt/set-marketing-budget`, activity 2 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Read What Customers Read Before a Case**
  - `ref/sup/find-gaps-in-the-help-center`, activity 4 -
    [Find Gaps in the Help Center](../../../../processes/customer-support/find-gaps-in-the-help-center.md)
- **Read the Behavioral Record**
  - `ref/mkt/buyer-persona`, activity 4 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
  - `ref/mkt/map-buyer-journey`, activity 2 -
    [Map Buyer Journey](../../../../processes/marketing/map-buyer-journey.md)
- **Read the Cases by Topic**
  - `ref/sup/report-what-customers-say`, activity 2 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Read the Customer Record**
  - `ref/mkt/ideal-customer-profile`, activity 2 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
  - `ref/mkt/segment-the-market`, activity 3 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Read the Exception Queue**
  - `ref/mkt/lead-scoring-model`, activity 3 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Read the Headcount**
  - `ref/hr/report-on-the-workforce`, activity 3 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Read the Hires and Leavers**
  - `ref/hr/report-on-the-workforce`, activity 4 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Read the History of Requests**
  - `ref/sup/forecast-support-volume`, activity 2 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Read the Labor Cost**
  - `ref/hr/plan-the-workforce`, activity 4 -
    [Plan the Workforce](../../../../processes/human-resources/plan-the-workforce.md)
  - `ref/hr/report-on-the-workforce`, activity 5 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Read the Product's Own Record**
  - `ref/mkt/product-positioning`, activity 4 -
    [Develop Product Positioning](../../../../processes/marketing/product-positioning.md)
- **Read the Reasons for Leaving**
  - `ref/hr/report-on-the-workforce`, activity 6 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)
- **Read the Time Each Case Takes**
  - `ref/sup/forecast-support-volume`, activity 8 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Read the Year's Hiring and Leaving**
  - `ref/hr/plan-the-workforce`, activity 3 -
    [Plan the Workforce](../../../../processes/human-resources/plan-the-workforce.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
