---
name: write-ad-copy-inside-each-placement-limit
description: The agent writes headlines and body that fit inside the character and size limits each placement sets, produces enough versions to rotate or to test, and puts in the lines a market requires the ad to carry. Use it when running `ref/mkt/conversion-experiment` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: copywriter
  agent-version: "1"
---

# Write ad copy inside each placement limit

## What it does

The agent writes headlines and body that fit inside the character and
size limits each placement sets, produces enough versions to rotate or
to test, and puts in the lines a market requires the ad to carry.

## Where it happens

The agent does this in six activities across six reference processes.
Each one names the activity as that process words it.

- **Add the Disclosures Each Market Requires**
  - `ref/mkt/traffic-ad-creative`, activity 6 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Make the Ad Set**
  - `ref/mkt/display-retargeting`, activity 9 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Produce the Variants**
  - `ref/mkt/conversion-experiment`, activity 6 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
  - `ref/mkt/test-ad-creative`, activity 8 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Size for Every Channel**
  - `ref/mkt/creative-assets`, activity 10 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
- **Write the Ads**
  - `ref/mkt/paid-search-campaign`, activity 4 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Write the Text for Each Placement**
  - `ref/mkt/traffic-ad-creative`, activity 5 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

Every draft at a version, and the DONE records of the patterns it works
inside. A claim it uses cites the register entry it came from.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
