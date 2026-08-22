---
name: score-an-email
description: Scores a message the way a subscriber will receive it, checking how it renders, whether its images carry alt text, and whether the contrast and the reading order hold in the clients people actually read it in. Use it when running `ref/mkt/customer-newsletter` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score an email

## What it does

Scores a message the way a subscriber will receive it, checking how it
renders, whether its images carry alt text, and whether the contrast and
the reading order hold in the clients people actually read it in.

## Where it happens

The agent does this in three activities across four reference processes.
Each one names the activity as that process words it.

- **Check and Sign What Was Made**
  - `ref/mkt/onboarding-email-program`, activity 7 -
    [Run Onboarding Email Program](../../../../processes/marketing/onboarding-email-program.md)
- **Proof the Issue**
  - `ref/mkt/customer-newsletter`, activity 11 -
    [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- **Score the Messages**
  - `ref/mkt/nurture-sequence`, activity 9 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
  - `ref/mkt/win-back-campaign`, activity 10 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
