---
name: build-the-list-a-run-sends-to
description: Builds the list a run will reach and takes out everyone the consent record does not cover, then delivers that list wherever it has to go, whether that is an invitation, a notice per treatment, an approach to candidates or an audience loaded into the systems that serve ads. Use it when running `ref/mkt/channel-program` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: consent-manager
  agent-version: "1"
---

# Build the list a run sends to

## What it does

Builds the list a run will reach and takes out everyone the consent
record does not cover, then delivers that list wherever it has to go,
whether that is an invitation, a notice per treatment, an approach to
candidates or an audience loaded into the systems that serve ads.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Apply Consent and Suppression**
  - `ref/mkt/target-audience-segment`, activity 9 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Build the Invitation Audience**
  - `ref/mkt/webinar`, activity 7 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Build the Notice Lists**
  - `ref/mkt/pricing-change`, activity 9 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Load the Audiences the Plan Names**
  - `ref/mkt/traffic-ad-creative`, activity 11 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Open Recruitment**
  - `ref/mkt/channel-program`, activity 11 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)

## What to record

For every list it clears, the count it removed and the rule each removal
was made under. For every withdrawal, a dated line naming each system
that keeps a copy of the audience, when the withdrawal was written into
it, and when the write was confirmed. A verdict per item for a scored
change, each citing the rule and its version. For every send it stopped,
the rule the send would have broken and the contacts it would have
reached.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
