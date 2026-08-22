---
name: verify-what-is-actually-running
description: "The agent reads what is live and compares it against what was set up: whether every version is still running and the split holds, whether the material renders and the clicks reach the destination, and whether what was excluded has stopped appearing. Use it when running `ref/mkt/test-ad-creative`, `ref/mkt/traffic-ad-creative` and `ref/mkt/verify-ad-placement`."
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Verify what is actually running

## What it does

The agent reads what is live and compares it against what was set up:
whether every version is still running and the split holds, whether the
material renders and the clicks reach the destination, and whether what
was excluded has stopped appearing.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check the Live Ads**
  - `ref/mkt/traffic-ad-creative`, activity 16 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Confirm the Exclusions Hold**
  - `ref/mkt/verify-ad-placement`, activity 11 -
    [Verify Ad Placement Quality](../../../../processes/marketing/verify-ad-placement.md)
- **Watch Delivery**
  - `ref/mkt/test-ad-creative`, activity 14 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
