---
name: route-leads-to-their-owners
description: Works out who owns a lead from its territory and its score, assigns it, and tells that owner with the score and the evidence behind it. Use it when running `ref/mkt/account-based-play` and 8 other reference processes.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Route leads to their owners

## What it does

Works out who owns a lead from its territory and its score, assigns it,
and tells that owner with the score and the evidence behind it. The same
work runs over a batch of leads that came from an event, a campaign, a
program or a list shared with another party.

## Where it happens

The agent does this in ten activities across nine reference processes.
Each one names the activity as that process words it.

- **Follow up with the People Who Came**
  - `ref/mkt/field-event`, activity 14 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Hand off the Leads**
  - `ref/mkt/webinar`, activity 16 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Hand over the Accounts that Moved**
  - `ref/mkt/account-based-play`, activity 17 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Hand over the Leads**
  - `ref/mkt/trade-show`, activity 13 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Hand over the Ready Ones**
  - `ref/mkt/nurture-sequence`, activity 15 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Hand over the Responders**
  - `ref/mkt/win-back-campaign`, activity 16 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)
- **Hand over the Selling Kit**
  - `ref/mkt/enable-channel-partner`, activity 13 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Notify**
  - `ref/mkt/lead-routing`, activity 5 -
    [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)
- **Route**
  - `ref/mkt/lead-routing`, activity 4 -
    [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)
- **Split and Hand over the Leads**
  - `ref/mkt/co-marketing-campaign`, activity 14 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
