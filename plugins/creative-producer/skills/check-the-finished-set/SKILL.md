---
name: check-the-finished-set
description: "The agent reads the finished pieces together and says item by item what has to change: where they disagree with each other, where a sized version broke, and where a variant changed something it should not have. Use it when running `ref/mkt/creative-assets`, `ref/mkt/test-ad-creative` and `ref/mkt/video-asset`."
license: CC-BY-4.0
metadata:
  agent: creative-producer
  agent-version: "1"
---

# Check the finished set

## What it does

The agent reads the finished pieces together and says item by item what
has to change: where they disagree with each other, where a sized
version broke, and where a variant changed something it should not have.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Set Holds Together**
  - `ref/mkt/creative-assets`, activity 7 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
- **Check the Sized Set**
  - `ref/mkt/creative-assets`, activity 11 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
- **Check the Variant Set**
  - `ref/mkt/test-ad-creative`, activity 9 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Review the Cut**
  - `ref/mkt/video-asset`, activity 8 -
    [Produce Video Asset](../../../../processes/marketing/video-asset.md)

## What to record

The production plan at a version, saying what each agent owes and when
it is due. The CONVENED and DONE records of the briefing, the bake-off
and the approval. A dated record each time a piece lands or slips. The
delivered set, naming every asset at the version the signers approved.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
