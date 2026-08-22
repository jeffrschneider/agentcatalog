---
name: take-in-the-request
description: Takes a request for a piece and settles what it has to do, who it is for, what it asks a reader to do, and the date it is due. Use it when running `ref/mkt/customer-newsletter` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: content-manager
  agent-version: "1"
---

# Take in the request

## What it does

Takes a request for a piece and settles what it has to do, who it is
for, what it asks a reader to do, and the date it is due.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Open the Issue**
  - `ref/mkt/customer-newsletter`, activity 1 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- **Set the Parameters**
  - `ref/mkt/landing-page`, activity 2 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Take in the Request**
  - `ref/mkt/landing-page`, activity 1 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
  - `ref/mkt/website-content-update`, activity 1 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Take in the Topic**
  - `ref/mkt/long-form-content`, activity 1 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)

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
