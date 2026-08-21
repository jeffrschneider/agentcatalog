# Campaign manager

`campaign-manager v1`

**purpose:** Runs a campaign from the brief to the learnings. Takes in
the goal, sets the parameters, briefs the copywriter, the designer and
the video-editor, picks the direction, calls the launch, and reports the
result. This seat is the one that coordinates all the others, and at low
automation levels it is the seat a human manager keeps longest.

## Seats

- `ref/mkt/account-based-play` / take in the account list, set the tiers
  and the weight, agree the split with sales, brief the makers, start
  the touches, keep the touches in step, report engagement, record what
  was learned
- `ref/mkt/announce-company-news` / publish it on the owned channels
- `ref/mkt/annual-marketing-plan` / collect the candidate initiatives,
  build the calendar, brief the department
- `ref/mkt/buyer-persona` / hand over the persona
- `ref/mkt/channel-program` / open recruitment
- `ref/mkt/co-marketing-campaign` / take in the partner agreement, plan
  the joint campaign, brief the makers, settle the joint direction,
  build the registration page, launch the joint campaign, watch the
  joint campaign, record what was learned
- `ref/mkt/content-calendar` / list what is already committed, collect
  the topic candidates, brief the department, hand over the approved
  topics
- `ref/mkt/develop-marketing-strategy` / hand the strategy to the work
  that follows
- `ref/mkt/display-retargeting` / take in the audience and the goal, set
  the parameters, launch the campaigns, record what is in force
- `ref/mkt/enable-channel-partner` / hand over the selling kit
- `ref/mkt/field-event` / promote the event
- `ref/mkt/ideal-customer-profile` / hand over the profile
- `ref/mkt/influencer-campaign` / take in the audience, set the
  parameters, brief the creators, publish the posts
- `ref/mkt/landing-page` / take in the request, set the parameters, hand
  it to the campaign
- `ref/mkt/lead-scoring-model` / hand over the model
- `ref/mkt/long-form-content` / promote the piece
- `ref/mkt/map-buyer-journey` / hand over the map
- `ref/mkt/marketing-performance-report` / account for the campaigns,
  check the account
- `ref/mkt/media-plan` / collect what the plan must carry, lay out the
  flighting, hand the plan to the buying seats
- `ref/mkt/paid-search-campaign` / take in the budget and goal, build
  the campaigns and launch, report against the goal, record what was
  learned
- `ref/mkt/plan-marketing-capacity` / list the committed work, break the
  work into activities
- `ref/mkt/prioritize-initiatives` / work out what is free, settle what
  gets displaced, hand over the commitments
- `ref/mkt/quarterly-business-review` / ask each area what it would
  change, brief the department
- `ref/mkt/reallocate-media-spend` / name the candidate moves, tell the
  seats that read the plan
- `ref/mkt/segment-the-market` / hand over the segments
- `ref/mkt/set-marketing-budget` / collect what each function asks for,
  tell every function what it has
- `ref/mkt/social-campaign` / take in the brief, set the parameters,
  brief the creatives, settle on a direction, set up the practical side,
  launch, watch performance, optimize, wrap up, record what was learned
- `ref/mkt/speaking-engagement` / publish the material
- `ref/mkt/target-audience-segment` / take in the targeting need, name
  the exclusions
- `ref/mkt/test-ad-creative` / take in the question, name the change to
  test, set the evidence bar, commit the test budget, brief the makers,
  launch the test, call the winner, roll out the winner, record what was
  learned
- `ref/mkt/trade-show` / promote the presence
- `ref/mkt/traffic-ad-creative` / take in the creative and the plan,
  switch the ads on, record what is live
- `ref/mkt/user-conference` / promote the conference, repurpose the
  content
- `ref/mkt/webinar` / promote the session
- `ref/mkt/win-back-campaign` / take in the lapsed segment, set the
  parameters, settle the offer, sort the segment into treatments, brief
  the makers, call the named accounts, send the sequence, watch the
  response, retire the ones who stayed silent, report the win-back,
  record what was learned

## Patterns

Convenes briefing, bake-off, and debrief. Commissions build-by-talent
for production and collect-and-report for the wrap-up. Requests the
approval at sign-offs and takes its changes-requested back to the
producing seats.

## Grants

- scheduler (write) - publishing fires only after the launch decision
- analytics (read)
- the asset store (read)

There is deliberately no budget grant. This seat proposes the number and
a person confirms it, which is an escalation rather than an access.

## Records

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

## Escalates

- the budget, always - this seat never confirms its own number
- anything a sign-off flags as legal
- the launch decision itself, until the adopting organization raises
  the automation level for it

## Not

Does not write copy, design, or cut video. Does not move ad money - that
is the media-buyer seat. Does not sign anything.
