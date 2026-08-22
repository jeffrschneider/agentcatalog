---
name: score-a-page
description: Reads a page as it will actually be served and scores it against the standards in force, covering alt text, contrast, heading order, keyboard use, load time, broken links, the title and the tracking on it. Use it when running `ref/mkt/customer-case-study` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score a page

## What it does

Reads a page as it will actually be served and scores it against the
standards in force, covering alt text, contrast, heading order, keyboard
use, load time, broken links, the title and the tracking on it. Every
failure cites the rule it was scored against.

## Where it happens

The agent does this in five activities across six reference processes.
Each one names the activity as that process words it.

- **Check the Changed Page**
  - `ref/mkt/website-content-update`, activity 10 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Check the Changed Pages**
  - `ref/mkt/refresh-content`, activity 18 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)
- **Check the Finished Page**
  - `ref/mkt/customer-case-study`, activity 17 -
    [Produce Customer Case Study](../../../../processes/marketing/customer-case-study.md)
  - `ref/mkt/long-form-content`, activity 13 -
    [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- **Open Registration**
  - `ref/mkt/user-conference`, activity 7 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Score the Page**
  - `ref/mkt/landing-page`, activity 9 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
