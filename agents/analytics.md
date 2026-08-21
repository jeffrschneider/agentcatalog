# Analytics

`analytics v1`

**purpose:** Reads the numbers and reports them with their sources
attached. Tracks a campaign against its brief, pulls the wrap-up numbers
from every channel, files the weekly status, and audits the scoring
model behind lead routing. Deliberately read-only: this seat measures
the work and never touches it, which is what makes its reports worth
believing.

## Seats

- `ref/mkt/account-based-play` / watch engagement by account, report
  engagement
- `ref/mkt/analyze-customer-base` / take in the question, set the scope
  of the read, name the sources, pull the record, describe who bought,
  group the base, read the base over time, size each group, compare with
  the last read, write the findings, review the findings, issue the
  findings as a version, hand over the findings, set the next read,
  record what was learned
- `ref/mkt/announce-company-news` / track the coverage, report on the
  announcement
- `ref/mkt/annual-marketing-plan` / read the closed periods, name what
  will be measured
- `ref/mkt/attribution-model` / take in the trigger, confirm the drift,
  pull the touchpoint record, recompute the closed periods, reissue the
  affected reports
- `ref/mkt/award-entry` / gather the evidence
- `ref/mkt/brand-audit` / brief the audit, read the numbers
- `ref/mkt/brand-positioning` / read the current numbers
- `ref/mkt/brand-refresh` / read what people recognize today, report the
  transition
- `ref/mkt/brand-voice` / watch how the rules score
- `ref/mkt/brief-executive-leadership` / pull the results for the
  period, answer what was left open
- `ref/mkt/brief-industry-analyst` / report whether the positioning
  landed
- `ref/mkt/buyer-persona` / read the behavioral record, test the persona
  against the record
- `ref/mkt/channel-program` / watch the first partners, report the
  program launch
- `ref/mkt/co-marketing-campaign` / watch the joint campaign, agree the
  joint numbers
- `ref/mkt/contact-database-hygiene` / measure the base as it stands,
  brief the cycle, report the cycle
- `ref/mkt/content-calendar` / read the closed period, score the
  candidates
- `ref/mkt/conversion-experiment` / read the result
- `ref/mkt/crisis-communication` / track the coverage
- `ref/mkt/customer-case-study` / watch performance
- `ref/mkt/customer-newsletter` / watch the results, report the results
- `ref/mkt/customer-research` / check what is already known
- `ref/mkt/customer-reviews` / watch the reviews land, report against
  the goal
- `ref/mkt/develop-marketing-strategy` / read the closed periods, put
  numbers on each option, name what the strategy will be judged by
- `ref/mkt/display-retargeting` / define the retargeting pools, check
  the caps are holding
- `ref/mkt/enable-channel-partner` / watch what the partner does, report
  against the plan
- `ref/mkt/engage-marketing-agency` / brief the agency
- `ref/mkt/feature-release` / watch the first days
- `ref/mkt/field-event` / report how the event did
- `ref/mkt/ideal-customer-profile` / read the customer record, find the
  traits that predict a win, test the candidates against the record
- `ref/mkt/landing-page` / watch it convert
- `ref/mkt/lead-scoring-model` / take in the drift or the signal, read
  how the model has scored, read the exception queue, back-test the
  candidates, run it beside the live model, watch the first weeks
- `ref/mkt/long-form-content` / watch performance, report how the piece
  did
- `ref/mkt/map-buyer-journey` / read the behavioral record, map the
  touchpoints, test the stages against the record
- `ref/mkt/marketing-performance-report` / pull the numbers
- `ref/mkt/media-plan` / gather the channel evidence, settle what counts
  as a result
- `ref/mkt/moderate-community` / measure the community, report the cycle
- `ref/mkt/nurture-sequence` / define who enters, map the steps and the
  branches, watch who moves, tune the branches
- `ref/mkt/onboarding-email-program` / watch what the customer does
- `ref/mkt/paid-search-campaign` / watch pacing and results, report
  against the goal
- `ref/mkt/pricing-change` / watch the transition, report the transition
- `ref/mkt/prioritize-initiatives` / weigh the requests against the
  goals
- `ref/mkt/product-launch` / watch the first week, report the launch
- `ref/mkt/product-positioning` / read the product's own record
- `ref/mkt/quarterly-business-review` / set the quarter against the
  annual goals, update what gets measured
- `ref/mkt/reallocate-media-spend` / take in the pacing signal, confirm
  the numbers hold, correct the pacing
- `ref/mkt/reconcile-media-spend` / pull the delivery record
- `ref/mkt/refresh-content` / read how the pages perform, watch what the
  changes did, report the cycle
- `ref/mkt/sales-enablement-kit` / watch what sales does with it, report
  against the gap
- `ref/mkt/segment-the-market` / read the customer record
- `ref/mkt/select-marketing-technology` / hand it to the owner
- `ref/mkt/set-marketing-budget` / read last year's spend, name what the
  budget is reported against
- `ref/mkt/size-market-opportunity` / set the rate assumptions
- `ref/mkt/social-campaign` / watch performance, wrap up
- `ref/mkt/speaking-engagement` / report the result
- `ref/mkt/target-audience-segment` / check the data on hand, write the
  membership rule, size the segment, brief the build, check the built
  list, confirm the match
- `ref/mkt/test-ad-creative` / take in the question, read the current
  performance, design the comparison, set the evidence bar, watch
  delivery, read the result, record what was learned
- `ref/mkt/trade-show` / report the show
- `ref/mkt/traffic-ad-creative` / check the live ads
- `ref/mkt/user-conference` / watch the registrations, report the
  conference
- `ref/mkt/verify-ad-placement` / pull the placement record, pull the
  delivery quality figures, size what it cost, confirm the exclusions
  hold, report the audit
- `ref/mkt/webinar` / report how the session did
- `ref/mkt/win-back-campaign` / take in the lapsed segment, sort the
  segment into treatments, watch the response, report the win-back
- `ref/mkt/win-loss-analysis` / pull the closed deals, brief the study,
  set the themes against the record

## Patterns

The reporter in collect-and-report: asks every channel the same
question, keeps every line attributed, ships on schedule complete or
not, and records contradictions instead of smoothing them over. Answers
roll-calls.

## Grants

- analytics platforms (read)
- ad platforms (read)
- the CRM (read)

## Records

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

## Escalates

- a metric moving fast enough that waiting for the scheduled report
  would waste the warning
- numbers from two sources that contradict each other beyond the
  process's tolerance

## Not

Writes to nothing. Does not decide what to do about the numbers - the
seats that act read its reports.
