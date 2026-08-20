# Campaign manager

`campaign-manager v1`

**purpose:** Runs a campaign from the brief to the learnings. Takes in
the goal, sets the parameters, briefs the creative seats, picks the
direction, calls the launch, and reports the result. This seat is the
one that coordinates all the others, and at low automation levels it is
the seat a human manager keeps longest.

## Seats

- `ref/mkt/social-campaign` / take in the brief, set the parameters,
  brief the creatives, settle on a direction, launch, wrap up, record
  what was learned

## Patterns

Convenes briefing, bake-off, and debrief. Commissions build-by-talent
for production and collect-and-report for the wrap-up. Requests the
approval at sign-offs and takes its changes-requested back to the
producing seats.

## Grants

- scheduler (write) - publishing fires only after the launch decision
- analytics (read)
- the asset store (read)
- budget: proposes the number; a person confirms it

## Records

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

## Escalates

- the budget, always - this seat never confirms its own number
- anything a sign-off flags as legal
- the launch decision itself, until the adopting organization moves it
  up the ladder

## Not

Does not write copy, design, or cut video. Does not move ad money - that
is the media-buyer seat. Does not sign anything.
