---
name: deliver-the-list
description: The agent applies the consent record and the field limits to the approved list, formats it for the receiving system, sends it, and gets a receipt back saying what was accepted and what was rejected. Use it when running `ref/mkt/account-based-play` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: audience-handover
  agent-version: "1"
---

# Deliver the list

## What it does

The agent applies the consent record and the field limits to the
approved list, formats it for the receiving system, sends it, and gets a
receipt back saying what was accepted and what was rejected.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Hand over the Selling Kit**
  - `ref/mkt/enable-channel-partner`, activity 13 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Hand the List to the Platforms**
  - `ref/mkt/target-audience-segment`, activity 13 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Load the Audiences the Plan Names**
  - `ref/mkt/traffic-ad-creative`, activity 11 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Set up the Paid Buy**
  - `ref/mkt/account-based-play`, activity 11 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Split and Hand over the Leads**
  - `ref/mkt/co-marketing-campaign`, activity 14 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)

## What to record

For every transfer: the list at the version it was approved at, the
count it started with, the count the consent record took out, the fields
that were sent, and the fields that were held back with the term that
held each one back. The date and time the transfer went, the count the
receiving system accepted, the count it rejected with the reason it
gave, and how much of the list matched. The approval the transfer rests
on, naming the person who signed for it. The date the receiving
organization is required to delete the records, taken from the
agreement. A dated line for every withdrawal passed on after the
transfer, naming the system it went to and the day that system confirmed
it. A transfer whose receipt never arrived is recorded as unconfirmed
rather than left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
