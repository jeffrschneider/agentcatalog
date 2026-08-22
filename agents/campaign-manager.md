# Campaign manager

`campaign-manager v1`

**purpose:** Runs a campaign from the brief to the learnings. Takes in
the goal, sets the parameters, briefs the copywriter, the designer and
the video-editor, picks the direction, calls the launch, and reports the
result. This agent is the one that coordinates all the others, and at
low automation levels it is the agent a human manager keeps longest.

## Processes

- `ref/mkt/account-based-play` / Take in the Account List, Set the Tiers
  and the Weight, Agree the Split with Sales, Brief the Makers, Start
  the Touches, Keep the Touches in Step, Report Engagement, Record What
  Was Learned
- `ref/mkt/announce-company-news` / Publish It on the Owned Channels
- `ref/mkt/annual-marketing-plan` / Collect the Candidate Initiatives,
  Build the Calendar, Brief the Department
- `ref/mkt/buyer-persona` / Hand over the Persona
- `ref/mkt/channel-program` / Open Recruitment
- `ref/mkt/co-marketing-campaign` / Take in the Partner Agreement, Plan
  the Joint Campaign, Brief the Makers, Settle the Joint Direction,
  Build the Registration Page, Launch the Joint Campaign, Watch the
  Joint Campaign, Record What Was Learned
- `ref/mkt/content-calendar` / List What Is Already Committed, Collect
  the Topic Candidates, Brief the Department, Hand over the Approved
  Topics
- `ref/mkt/develop-marketing-strategy` / Hand the Strategy to the Work
  that Follows
- `ref/mkt/display-retargeting` / Take in the Audience and the Goal, Set
  the Parameters, Launch the Campaigns, Record What Is in Force
- `ref/mkt/enable-channel-partner` / Hand over the Selling Kit
- `ref/mkt/field-event` / Promote the Event
- `ref/mkt/ideal-customer-profile` / Hand over the Profile
- `ref/mkt/influencer-campaign` / Take in the Audience, Set the
  Parameters, Brief the Creators, Publish the Posts
- `ref/mkt/landing-page` / Take in the Request, Set the Parameters, Hand
  It to the Campaign
- `ref/mkt/lead-scoring-model` / Hand over the Model
- `ref/mkt/long-form-content` / Promote the Piece
- `ref/mkt/map-buyer-journey` / Hand over the Map
- `ref/mkt/marketing-performance-report` / Account for the Campaigns,
  Check the Account
- `ref/mkt/media-plan` / Collect What the Plan Must Carry, Lay out the
  Flighting, Hand the Plan to the Buying Agents
- `ref/mkt/paid-search-campaign` / Take in the Budget and Goal, Build
  the Campaigns and Launch, Report against the Goal, Record What Was
  Learned
- `ref/mkt/plan-marketing-capacity` / List the Committed Work, Break the
  Work into Activities
- `ref/mkt/prioritize-initiatives` / Work out What Is Free, Settle What
  Gets Displaced, Hand over the Commitments
- `ref/mkt/quarterly-business-review` / Ask Each Area What It Would
  Change, Brief the Department
- `ref/mkt/reallocate-media-spend` / Name the Candidate Moves, Tell the
  Agents that Read the Plan
- `ref/mkt/segment-the-market` / Hand over the Segments
- `ref/mkt/set-marketing-budget` / Collect What Each Function Asks For,
  Tell Every Function What It Has
- `ref/mkt/social-campaign` / Take in the Brief, Set the Parameters,
  Brief the Creatives, Settle on a Direction, Set up the Practical Side,
  Launch, Watch Performance, Optimize, Wrap Up, Record What Was Learned
- `ref/mkt/speaking-engagement` / Publish the Material
- `ref/mkt/target-audience-segment` / Take in the Targeting Need, Name
  the Exclusions
- `ref/mkt/test-ad-creative` / Take in the Question, Name the Change to
  Test, Set the Evidence Bar, Commit the Test Budget, Brief the Makers,
  Launch the Test, Call the Winner, Roll out the Winner, Record What Was
  Learned
- `ref/mkt/trade-show` / Promote the Presence
- `ref/mkt/traffic-ad-creative` / Take in the Creative and the Plan,
  Switch the Ads On, Record What Is Live
- `ref/mkt/user-conference` / Promote the Conference, Repurpose the
  Content
- `ref/mkt/webinar` / Promote the Session
- `ref/mkt/win-back-campaign` / Take in the Lapsed Segment, Set the
  Parameters, Settle the Offer, Sort the Segment into Treatments, Brief
  the Makers, Call the Named Accounts, Send the Sequence, Watch the
  Response, Retire the Ones Who Stayed Silent, Report the Win-Back,
  Record What Was Learned

## Patterns

Convenes briefing, bake-off, and debrief. Commissions build-by-talent
for production and collect-and-report for the wrap-up. Requests the
approval at sign-offs and takes its changes-requested back to the
producing agents.

## Grants

- scheduler (write) - publishing fires only after the launch decision
- analytics (read)
- the asset store (read)

There is deliberately no budget grant. This agent proposes the number
and a person confirms it, which is an escalation rather than an access.

## Records

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

## Escalates

- the budget, always - this agent never confirms its own number
- anything a sign-off flags as legal
- the launch decision itself, until the adopting organization raises the
  automation level for it

## Not

Does not write copy, design, or cut video. Does not move ad money - that
is the media-buyer agent. Does not sign anything.
