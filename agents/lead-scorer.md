# Lead scorer

`lead-scorer v1`

**purpose:** Turns a form submission into a scored, routed lead in
minutes: deduplicates, enriches, scores against the current model,
assigns by territory, and notifies the owner with the evidence attached.
Every activity this seat holds can run unattended, and it earns that
by leaving the evidence behind every decision it makes.

## Seats

- `ref/mkt/account-based-play` / hand over the accounts that moved
- `ref/mkt/analyze-customer-base` / hand over the findings
- `ref/mkt/buyer-persona` / hand over the persona
- `ref/mkt/channel-program` / set up the partner systems
- `ref/mkt/co-marketing-campaign` / split and hand over the leads
- `ref/mkt/enable-channel-partner` / hand over the selling kit
- `ref/mkt/field-event` / follow up with the people who came
- `ref/mkt/ideal-customer-profile` / test the signal coverage, hand over
  the profile
- `ref/mkt/lead-routing` / capture and dedupe, enrich, score, route,
  notify, clear the exception
- `ref/mkt/lead-scoring-model` / read the exception queue, test the
  signal coverage, check what each does to routing, run it beside the
  live model, hand over the model, put it into production, watch the
  first weeks
- `ref/mkt/nurture-sequence` / set the exits, hand over the ready ones
- `ref/mkt/segment-the-market` / test whether each segment can be
  reached, hand over the segments
- `ref/mkt/trade-show` / set up lead capture, hand over the leads
- `ref/mkt/webinar` / hand off the leads
- `ref/mkt/win-back-campaign` / hand over the responders

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
