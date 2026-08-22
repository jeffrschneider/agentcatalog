---
name: handle-a-change-to-a-live-page
description: Takes a change against a page that is already live, works out whether it is a small edit or needs a bigger run and who has to sign it, makes the change the request or the numbers call for, and closes it when the requester agrees. Use it when running `ref/mkt/landing-page` and `ref/mkt/website-content-update`.
license: CC-BY-4.0
metadata:
  agent: content-manager
  agent-version: "1"
---

# Handle a change to a live page

## What it does

Takes a change against a page that is already live, works out whether it
is a small edit or needs a bigger run and who has to sign it, makes the
change the request or the numbers call for, and closes it when the
requester agrees.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Close out the Change**
  - `ref/mkt/website-content-update`, activity 12 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Fix What the Numbers Show**
  - `ref/mkt/landing-page`, activity 14 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Route the Change**
  - `ref/mkt/website-content-update`, activity 3 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)

## What to record

The request as it was accepted, with the date the piece promised and
what the piece is meant to accomplish. The CONVENED and DONE records of
everything it convenes. The publish record, naming who said go and which
version went live. The performance readout at the cadence the process
sets, and the decision it made after reading that readout: leave the
piece alone, update it, or retire it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
