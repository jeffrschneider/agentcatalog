---
name: report-against-what-was-promised
description: When a run, a period or a campaign is over, the agent sets what happened beside what was promised and reports the difference, with the source on every line. Use it when running `ref/mkt/account-based-play` and 28 other reference processes.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Report against what was promised

## What it does

When a run, a period or a campaign is over, the agent sets what happened
beside what was promised and reports the difference, with the source on
every line. Where two sides kept their own counts, it matches them into
one set of figures.

## Where it happens

The agent does this in 24 activities across 29 reference processes. Each
one names the activity as that process words it.

- **Agree the Joint Numbers**
  - `ref/mkt/co-marketing-campaign`, activity 15 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Read the Closed Period**
  - `ref/mkt/content-calendar`, activity 2 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Read the Closed Periods**
  - `ref/mkt/annual-marketing-plan`, activity 2 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/develop-marketing-strategy`, activity 2 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Report Engagement**
  - `ref/mkt/account-based-play`, activity 18 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Report How the Event Did**
  - `ref/mkt/field-event`, activity 15 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Report How the Piece Did**
  - `ref/mkt/long-form-content`, activity 17 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Report How the Session Did**
  - `ref/mkt/webinar`, activity 17 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Report Whether the Positioning Landed**
  - `ref/mkt/brief-industry-analyst`, activity 16 -
    [Brief Industry Analyst](../../../../processes/marketing/brief-industry-analyst.md)
- **Report against the Gap**
  - `ref/mkt/sales-enablement-kit`, activity 15 -
    [Produce Sales Enablement Kit](../../../../processes/marketing/sales-enablement-kit.md)
- **Report against the Goal**
  - `ref/mkt/customer-reviews`, activity 15 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
  - `ref/mkt/paid-search-campaign`, activity 12 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Report against the Plan**
  - `ref/mkt/enable-channel-partner`, activity 15 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Report on the Announcement**
  - `ref/mkt/announce-company-news`, activity 16 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
- **Report the Audit**
  - `ref/mkt/verify-ad-placement`, activity 14 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Report the Conference**
  - `ref/mkt/user-conference`, activity 16 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Report the Cycle**
  - `ref/mkt/contact-database-hygiene`, activity 16 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
  - `ref/mkt/moderate-community`, activity 14 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)
  - `ref/mkt/refresh-content`, activity 21 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Report the Launch**
  - `ref/mkt/product-launch`, activity 10 -
    [Launch Product](../../../../processes/marketing/product-launch.md)
- **Report the Program Launch**
  - `ref/mkt/channel-program`, activity 16 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
- **Report the Result**
  - `ref/mkt/speaking-engagement`, activity 15 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)
- **Report the Results**
  - `ref/mkt/customer-newsletter`, activity 16 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- **Report the Show**
  - `ref/mkt/trade-show`, activity 15 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Report the Transition**
  - `ref/mkt/brand-refresh`, activity 25 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
  - `ref/mkt/pricing-change`, activity 15 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Report the Win-Back**
  - `ref/mkt/win-back-campaign`, activity 19 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Set the Quarter against the Annual Goals**
  - `ref/mkt/quarterly-business-review`, activity 3 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Wrap Up**
  - `ref/mkt/social-campaign`, activity 12 -
    [Run Social Media Campaign](../../../../processes/marketing/social-campaign.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
