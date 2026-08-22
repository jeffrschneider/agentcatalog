---
name: score-material-before-it-goes-out
description: The agent reads a piece that is about to publish and scores it against the claims register and the guidelines at the versions in force. Use it when running `ref/mkt/approve-marketing-material` and 13 other reference processes.
license: CC-BY-4.0
metadata:
  agent: brand-check
  agent-version: "1"
---

# Score material before it goes out

## What it does

The agent reads a piece that is about to publish and scores it against
the claims register and the guidelines at the versions in force. It
returns a verdict on every rule with the evidence behind it, so a
sign-off only has to read the exceptions.

## Where it happens

The agent does this in thirteen activities across fourteen reference
processes. Each one names the activity as that process words it.

- **Check It Once**
  - `ref/mkt/feature-release`, activity 5 -
    [Announce Feature Release](../../../../processes/marketing/feature-release.md)
- **Check the Ask against the Rules**
  - `ref/mkt/customer-reviews`, activity 7 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Check the Sized Set**
  - `ref/mkt/creative-assets`, activity 11 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
- **Review the Drafts**
  - `ref/mkt/influencer-campaign`, activity 12 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)
- **Score against Both Rule Sets**
  - `ref/mkt/co-marketing-campaign`, activity 7 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Score against Brand and Claims**
  - `ref/mkt/approve-marketing-material`, activity 4 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Score against the Standards**
  - `ref/mkt/creative-assets`, activity 8 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
  - `ref/mkt/video-asset`, activity 11 -
    [Produce Video Asset](../../../../processes/marketing/video-asset.md)
- **Score the Adapted Set**
  - `ref/mkt/traffic-ad-creative`, activity 7 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Score the Change**
  - `ref/mkt/website-content-update`, activity 7 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Score the Claims**
  - `ref/mkt/competitive-battlecard`, activity 10 -
    [Refresh Competitive Battlecard](../../../../processes/marketing/competitive-battlecard.md)
- **Score the Kit**
  - `ref/mkt/sales-enablement-kit`, activity 10 -
    [Produce Sales Enablement Kit](../../../../processes/marketing/sales-enablement-kit.md)
- **Score the Messages**
  - `ref/mkt/nurture-sequence`, activity 9 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
  - `ref/mkt/win-back-campaign`, activity 10 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Score the Page**
  - `ref/mkt/landing-page`, activity 9 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)

## What to record

A score per item, each citing the standard, its version, and the rule
applied. What passed, what failed, and why, in a form the human signers
read in minutes.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
