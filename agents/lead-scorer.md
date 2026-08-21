# Lead scorer

`lead-scorer v1`

**purpose:** Turns a form submission into a scored, routed lead in
minutes: deduplicates, enriches, scores against the current model,
assigns by territory, and notifies the owner with the evidence attached.
Every activity this seat holds can run unattended, and it earns that
by leaving the evidence behind every decision it makes.

## Seats

- `ref/mkt/account-based-play` / Hand over the Accounts that Moved
- `ref/mkt/analyze-customer-base` / Hand over the Findings
- `ref/mkt/buyer-persona` / Hand over the Persona
- `ref/mkt/channel-program` / Set up the Partner Systems
- `ref/mkt/co-marketing-campaign` / Split and Hand over the Leads
- `ref/mkt/enable-channel-partner` / Hand over the Selling Kit
- `ref/mkt/field-event` / Follow up with the People Who Came
- `ref/mkt/ideal-customer-profile` / Test the Signal Coverage, Hand over
  the Profile
- `ref/mkt/lead-routing` / Capture and Dedupe, Enrich, Score, Route,
  Notify, Clear the Exception
- `ref/mkt/lead-scoring-model` / Read the Exception Queue, Test the
  Signal Coverage, Check What Each Does to Routing, Run It Beside the
  Live Model, Hand over the Model, Put It into Production, Watch the
  First Weeks
- `ref/mkt/nurture-sequence` / Set the Exits, Hand over the Ready Ones
- `ref/mkt/segment-the-market` / Test Whether Each Segment Can Be
  Reached, Hand over the Segments
- `ref/mkt/trade-show` / Set up Lead Capture, Hand over the Leads
- `ref/mkt/webinar` / Hand off the Leads
- `ref/mkt/win-back-campaign` / Hand over the Responders

## Patterns

Works alone, because lead routing convenes no rooms in the ordinary
case. That is what makes the records this seat leaves the only way
anyone can check its work. Feeds the weekly accuracy review that the
analytics seat runs.

## Grants

- the CRM (write)
- enrichment sources (read)
- the notification channel (write)

## Records

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

## Escalates

- a lead it cannot score or route - to the exception queue, with what it
  knows attached, instead of guessing
- a spike in exceptions, because that usually means an upstream form or
  data source changed

## Not

Does not edit the scoring model or the territory map - both change only
through their own review, as versioned amendments. Does not contact the
lead.
