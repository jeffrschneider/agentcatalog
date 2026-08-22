---
name: program-reporting
description: Reports what the program or a joint campaign returned against what was promised, matches both sides' counts and costs into one set of figures they agree on, and files what to repeat and what to avoid next time. Use it when running `ref/mkt/channel-program`, `ref/mkt/co-marketing-campaign` and `ref/mkt/enable-channel-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-manager
  agent-version: "1"
---

# Program reporting

## What it does

Reports what the program or a joint campaign returned against what was
promised, matches both sides' counts and costs into one set of figures
they agree on, and files what to repeat and what to avoid next time.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Agree the Joint Numbers**
  - `ref/mkt/co-marketing-campaign`, activity 15 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Record What Was Learned**
  - `ref/mkt/channel-program`, activity 17 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
  - `ref/mkt/co-marketing-campaign`, activity 16 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
  - `ref/mkt/enable-channel-partner`, activity 16 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Report the Program Launch**
  - `ref/mkt/channel-program`, activity 16 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)

## What to record

The partner record at a version, naming the agreement it rests on, the
tier the partner holds, the date that tier was set and who set it. For
everything the partner was given, the version it was at and the date it
went to them. For every person the partner put through training, what
they were trained on and the date they finished. A dated line for each
obligation as it comes due, saying whether it was met and by whom. What
the partner delivered back, counted against what the agreement asked
for, at the cadence the process sets. The CONVENED and DONE records of
everything it convenes, and the approval record behind every release and
every tier change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
