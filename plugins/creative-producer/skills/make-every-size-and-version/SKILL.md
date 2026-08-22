---
name: make-every-size-and-version
description: The agent reads what each placement takes and turns one approved master into every size, length and version that will actually run. Use it when running `ref/mkt/display-retargeting`, `ref/mkt/test-ad-creative` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: creative-producer
  agent-version: "1"
---

# Make every size and version

## What it does

The agent reads what each placement takes and turns one approved master
into every size, length and version that will actually run.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Cut the Creative to Every Specification**
  - `ref/mkt/traffic-ad-creative`, activity 4 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Make the Ad Set**
  - `ref/mkt/display-retargeting`, activity 9 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Produce the Variants**
  - `ref/mkt/test-ad-creative`, activity 8 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Read the Placement Specifications**
  - `ref/mkt/traffic-ad-creative`, activity 2 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

The production plan at a version, saying what each agent owes and when
it is due. The CONVENED and DONE records of the briefing, the bake-off
and the approval. A dated record each time a piece lands or slips. The
delivered set, naming every asset at the version the signers approved.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
