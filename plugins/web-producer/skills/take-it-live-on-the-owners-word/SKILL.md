---
name: take-it-live-on-the-owners-word
description: Waits for the named owner to say go, takes the staged work live on the date it was set for, and records what went live, at which version and who said go. Use it when running `ref/mkt/announce-company-news` and 12 other reference processes.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Take it live on the owners word

## What it does

Waits for the named owner to say go, takes the staged work live on the
date it was set for, and records what went live, at which version and
who said go.

## Where it happens

The agent does this in ten activities across thirteen reference
processes. Each one names the activity as that process words it.

- **Change the Public Price**
  - `ref/mkt/pricing-change`, activity 12 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Issue the Release**
  - `ref/mkt/announce-company-news`, activity 12 -
    [Announce Company News](../../../../processes/marketing/announce-company-news.md)
- **Issue the Response**
  - `ref/mkt/crisis-communication`, activity 11 -
    [Manage Crisis Communication](../../../../processes/marketing/crisis-communication.md)
- **Launch the Joint Campaign**
  - `ref/mkt/co-marketing-campaign`, activity 12 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Publish**
  - `ref/mkt/customer-case-study`, activity 18 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/landing-page`, activity 11 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
  - `ref/mkt/long-form-content`, activity 14 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Publish the Change**
  - `ref/mkt/website-content-update`, activity 11 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Publish the Changes**
  - `ref/mkt/refresh-content`, activity 19 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Publish the Material**
  - `ref/mkt/enable-channel-partner`, activity 9 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
  - `ref/mkt/speaking-engagement`, activity 14 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)
- **Publish the Version**
  - `ref/mkt/brand-guidelines`, activity 13 -
    [Publish Brand Guidelines](../../../../processes/marketing/brand-guidelines.md)
- **Switch the Properties**
  - `ref/mkt/brand-refresh`, activity 19 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
