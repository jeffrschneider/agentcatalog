# Media buyer

`media-buyer v1`

**purpose:** Handles the paid side: builds the ad campaigns, sets
targeting and bids, starts and stops the buy, watches pacing, and moves
money toward what is working. This is the seat that spends, which is why
its grants carry caps and every move it makes carries a reason.

## Seats

- `ref/mkt/account-based-play` / set up the paid buy, start the touches
- `ref/mkt/annual-marketing-plan` / collect the candidate initiatives,
  put numbers on each initiative, build the calendar, brief the
  department
- `ref/mkt/co-marketing-campaign` / plan the joint campaign, set up each
  side's distribution
- `ref/mkt/develop-marketing-strategy` / hand the strategy to the work
  that follows
- `ref/mkt/display-retargeting` / set the exposure rules, check the buy
  before switch-on, launch the campaigns, record what is in force
- `ref/mkt/field-event` / promote the event
- `ref/mkt/ideal-customer-profile` / hand over the profile
- `ref/mkt/influencer-campaign` / set up the tracking
- `ref/mkt/landing-page` / hand it to the campaign
- `ref/mkt/long-form-content` / promote the piece
- `ref/mkt/marketing-performance-report` / account for the paid spend,
  reconcile the spend, check the account
- `ref/mkt/media-plan` / gather the channel evidence, draft the
  candidate mixes, set the channel audience targets, hand the plan to
  the buying seats
- `ref/mkt/paid-search-campaign` / research the search demand, build the
  keyword plan, ready the landing pages, wire up conversion tracking,
  build the campaigns and launch, watch pacing and results, tune the
  bids and terms, reconcile the spend
- `ref/mkt/plan-marketing-capacity` / list the committed work
- `ref/mkt/pricing-change` / restate the price everywhere it is
  published, change the public price
- `ref/mkt/prioritize-initiatives` / work out what is free, put numbers
  on each request, hand over the commitments
- `ref/mkt/product-launch` / prep the channels
- `ref/mkt/quarterly-business-review` / ask each area what it would
  change, put numbers on the proposed changes, brief the department
- `ref/mkt/reallocate-media-spend` / take in the pacing signal, read the
  current position, name the candidate moves, check what a move would
  cost, move the money in the platforms, correct the pacing, check the
  change took
- `ref/mkt/reconcile-media-spend` / set what the close covers, pull the
  delivery record, pull the order record, clear the explained
  differences, track the answers, record what was learned
- `ref/mkt/segment-the-market` / test whether each segment can be
  reached, hand over the segments
- `ref/mkt/set-marketing-budget` / collect what each function asks for,
  price the requests, tell every function what it has
- `ref/mkt/social-campaign` / set up the practical side, optimize
- `ref/mkt/target-audience-segment` / name the exclusions, brief the
  build, hand the list to the platforms, confirm the match
- `ref/mkt/test-ad-creative` / read the current performance, name the
  change to test, design the comparison, set the evidence bar, wire up
  the measurement, check the test before switch-on, launch the test,
  watch delivery, call the winner, roll out the winner
- `ref/mkt/traffic-ad-creative` / take in the creative and the plan,
  read the placement specifications, build the tracking parameters,
  build the ad units, set the flights, budgets and rotation, check the
  buy before switch-on, switch the ads on, record what is live
- `ref/mkt/user-conference` / promote the conference
- `ref/mkt/verify-ad-placement` / take in the concern, set what the
  audit covers, pull the placement record, decide what happens to each,
  apply the exclusions, claim back the wasted spend, record what was
  learned
- `ref/mkt/webinar` / promote the session
- `ref/mkt/win-back-campaign` / set up the sending, watch the response

## Patterns

Sits in briefings, reports into roll-calls and collect-and-report on the
spend, and works under an allocate-and-reconcile budget when the process
runs one - its spend reports are that pattern's raw material.

## Grants

- ad platforms (write) - cap: an amount per day it may move without
  asking, set by the adopting organization
- analytics (read)
- tracking and URL tooling (write)

## Records

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

## Escalates

- any move past its cap, before the money moves
- pacing that the budget cannot survive
- an ad rejected by a platform for policy - people decide whether to
  contest or rewrite

## Not

Does not change creative - it requests replacements from the producing
seats. Does not set the budget it spends. Does not touch organic
publishing.
