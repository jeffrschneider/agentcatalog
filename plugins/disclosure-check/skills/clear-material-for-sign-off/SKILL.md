---
name: clear-material-for-sign-off
description: The agent puts its verdicts in front of the approval, so the named signers see what passed, what failed, and which rule each failure came from. Use it when running `ref/mkt/channel-program` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Clear material for sign off

## What it does

The agent puts its verdicts in front of the approval, so the named
signers see what passed, what failed, and which rule each failure came
from.

## Where it happens

The agent does this in one activity across five reference processes.
Each one names the activity as that process words it.

- **Get Sign-Offs**
  - `ref/mkt/channel-program`, activity 10 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
  - `ref/mkt/display-retargeting`, activity 10 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
  - `ref/mkt/enable-channel-partner`, activity 8 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
  - `ref/mkt/pricing-change`, activity 8 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
  - `ref/mkt/test-ad-creative`, activity 10 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

A verdict per item, each citing the rule, its version, the market it
applies in, and the version of the material it was read against. The
market and channel list the piece was scored against, recorded with the
score, so a later run into a new market is scored again. Where a rule
requires particular wording, the wording it requires, recorded beside
the item. A market the organization holds no rules for is recorded as
unscored. A rescore after a fix names what changed and what it ran
again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
