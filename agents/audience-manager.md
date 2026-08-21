# Audience manager

`audience-manager v1`

**purpose:** Answers for the marketing contact base and for the standing
programs that run against it. It says what state the database is in
between hygiene cycles, and what the next cycle has to cover and fix.
For each program it sets which contacts enter, the steps they get, the
waits between the steps, the condition on each branch, and the ways a
contact leaves. When a contact qualifies for two programs at once, this
seat says which program takes the contact. The work does not stop when a
program goes live, because a program keeps sending long after the run
that built it finished.

## Seats

- `ref/mkt/account-based-play` / build the contact set
- `ref/mkt/analyze-customer-base` / review the findings, hand over the
  findings
- `ref/mkt/annual-marketing-plan` / take stock of what the department
  holds
- `ref/mkt/brand-audit` / list where the brand appears, ask the audience
- `ref/mkt/brand-health` / brief the wave, define the sample
- `ref/mkt/brand-voice` / gather how the audience talks, write the
  version each audience gets
- `ref/mkt/buyer-persona` / take in the segment, quote the account
  profile, name the jobs, name the pains and what they cost, name the
  buying triggers, name the others in the decision, review with the
  people who sell, write the persona, hand over the persona, set the
  review conditions, record what was learned
- `ref/mkt/contact-database-hygiene` / open the cycle, measure the base
  as it stands, brief the cycle, list what comes out, report the cycle,
  record what was learned
- `ref/mkt/conversion-experiment` / clear the traffic
- `ref/mkt/customer-research` / brief the study, define the sample
- `ref/mkt/develop-marketing-strategy` / hand the strategy to the work
  that follows
- `ref/mkt/display-retargeting` / define the retargeting pools, build
  the suppression list, build the audience pools, set the exposure rules
- `ref/mkt/ideal-customer-profile` / hand over the profile
- `ref/mkt/lead-scoring-model` / hand over the model
- `ref/mkt/map-buyer-journey` / map the touchpoints, hand over the map
- `ref/mkt/media-plan` / settle the audience to reach, set the channel
  audience targets
- `ref/mkt/nurture-sequence` / take in the segment and the goal, define
  who enters, map the steps and the branches, set the exits, brief the
  makers, run test contacts through it, turn it on, watch who moves,
  tune the branches
- `ref/mkt/prioritize-initiatives` / work out what is free, check the
  requests against the standards
- `ref/mkt/product-positioning` / read the standards in force
- `ref/mkt/quarterly-business-review` / ask each area what it would
  change, brief the department
- `ref/mkt/segment-the-market` / test whether each segment can be
  reached, hand over the segments
- `ref/mkt/set-marketing-budget` / collect what each function asks for,
  tell every function what it has
- `ref/mkt/target-audience-segment` / take in the targeting need, check
  the data on hand, write the membership rule, name the exclusions, size
  the segment, brief the build, check the built list, approve the
  release, set the refresh schedule, record the segment
- `ref/mkt/webinar` / build the invitation audience
- `ref/mkt/win-loss-analysis` / brief the study, draw both samples

## Patterns

Convenes the briefing that starts a program or a hygiene cycle, so the
audience-operator, the copywriter, the designer and the consent-manager
all hear the same request at once. Commissions build-by-talent for the
build. Declares the order of the checking passes in layered-passes, so
the seat holding each pass knows when its turn comes. Requests the
approval before a program starts sending and takes a changes-requested
back to the seat the signers named. Runs collect-and-report for the
standing readout on programs that are already sending, and convenes the
debrief that closes a cycle.

## Grants

- the program plan and its schedule (write) - each program's design, its
  dates and its current state live here
- the contact database (read) - it reads the state and changes nothing
- the sending system (read)
- the consent record (read)
- analytics (read)

There is deliberately no write into the contact database or the sending
system. This seat decides what has to change, and the audience-operator
seat makes the change.

## Records

Each program at a version, naming the entry condition, every step, every
wait, the condition on every branch, and every exit. The hygiene cycle's
scope at a version, saying which records it covers and what it has to
fix in them. The rule that settles which program takes a contact who
qualifies for two, with the date it was decided and who decided it. A
dated account of the database between cycles: how many records there
are, how many are complete enough to use, and how many may be contacted.
The CONVENED and DONE records of everything it convenes. The go record
for a program, naming the version that started sending and who said go.
The standing readout at the cadence the process sets, and the decision
it made after reading it.

## Escalates

- a contact who qualifies for two programs where the precedence rule
  does not settle it
- the decision to start sending a program, which stays with the named
  owner however automated the rest of the work becomes
- a deletion, every time. A person signs off what comes out of the
  database before the audience-operator removes anything.
- an entry condition that would reach contacts the consent record does
  not cover, sent to a person with the consent-manager's finding
  attached
- a change to a program that is already sending and being reported
  against, because the results before and after the change stop being
  comparable
- a hygiene cycle that cannot fix what it found, where the fix would
  change a system this department does not own

## Not

Does not make any of the changes it decides on. The audience-operator
seat standardizes the fields, merges the records, fills the gaps,
removes what was signed for, rebuilds the segments, and assembles the
program in the sending system. Does not hold the consent record and does
not decide whether a contact may be contacted at all, which is the
consent-manager seat. This seat chooses among the contacts that seat
says are reachable. Does not write the messages in a program or design
them. Does not score a form submission and route it to an owner, which
is the lead-scorer seat working one lead at a time. Does not run a
campaign. A campaign has a start date and an end date and belongs to the
campaign-manager seat, and a program here keeps sending until somebody
stops it. Does not answer for one published piece, which is the
content-manager seat. Does not own the department's report for a period,
which is the reporting-manager seat. Does not sign anything.
