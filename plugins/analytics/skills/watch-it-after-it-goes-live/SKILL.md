---
name: watch-it-after-it-goes-live
description: Once something is live, the agent keeps reading what people do with it against the goal it was given, and reports what is happening while there is still time to act on it. Use it when running `ref/mkt/account-based-play` and 23 other reference processes.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Watch it after it goes live

## What it does

Once something is live, the agent keeps reading what people do with it
against the goal it was given, and reports what is happening while there
is still time to act on it.

## Where it happens

The agent does this in 21 activities across 24 reference processes. Each
one names the activity as that process words it.

- **Track the Coverage**
  - `ref/mkt/announce-company-news`, activity 15 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
  - `ref/mkt/crisis-communication`, activity 13 -
    [Manage Crisis Communication](../../../../processes/marketing/crisis-communication.md)
- **Watch Engagement by Account**
  - `ref/mkt/account-based-play`, activity 16 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Watch How the Rules Score**
  - `ref/mkt/brand-voice`, activity 18 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
- **Watch It Convert**
  - `ref/mkt/landing-page`, activity 13 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Watch Pacing and Results**
  - `ref/mkt/paid-search-campaign`, activity 9 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Watch Performance**
  - `ref/mkt/customer-case-study`, activity 20 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/long-form-content`, activity 16 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
  - `ref/mkt/social-campaign`, activity 9 -
    [Run Social Media Campaign](../../../../processes/marketing/social-campaign.md)
- **Watch What Sales Does with It**
  - `ref/mkt/sales-enablement-kit`, activity 14 -
    [Produce Sales Enablement Kit](../../../../processes/marketing/sales-enablement-kit.md)
- **Watch What the Changes Did**
  - `ref/mkt/refresh-content`, activity 20 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Watch What the Customer Does**
  - `ref/mkt/onboarding-email-program`, activity 10 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Watch What the Partner Does**
  - `ref/mkt/enable-channel-partner`, activity 14 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Watch Who Moves**
  - `ref/mkt/nurture-sequence`, activity 14 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Watch the First Days**
  - `ref/mkt/feature-release`, activity 10 -
    [Announce Feature Release](../../../../processes/marketing/feature-release.md)
- **Watch the First Partners**
  - `ref/mkt/channel-program`, activity 15 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
- **Watch the First Week**
  - `ref/mkt/product-launch`, activity 9 -
    [Launch Product](../../../../processes/marketing/product-launch.md)
- **Watch the First Weeks**
  - `ref/mkt/lead-scoring-model`, activity 16 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Watch the Joint Campaign**
  - `ref/mkt/co-marketing-campaign`, activity 13 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Watch the Registrations**
  - `ref/mkt/user-conference`, activity 9 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Watch the Response**
  - `ref/mkt/win-back-campaign`, activity 17 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Watch the Results**
  - `ref/mkt/customer-newsletter`, activity 14 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- **Watch the Reviews Land**
  - `ref/mkt/customer-reviews`, activity 13 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Watch the Transition**
  - `ref/mkt/pricing-change`, activity 14 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
