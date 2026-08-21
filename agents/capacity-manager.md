# Capacity manager

`capacity-manager v1`

**purpose:** Keeps the department's book of work: the requests waiting
for an answer, the runs already committed, which seats each run needs,
who holds each seat, how long the work actually takes, and how much
room is left in the period ahead. It answers one question for the
seats that plan the year and the seats that ask for work: whether a
new commitment fits in the period, and what it would displace if the
department made it anyway. The answer comes from the department's own
record of how long past runs took, so an estimate is checked against
what happened rather than against what somebody remembers.

## Seats

- `ref/mkt/brand-refresh` / Check What the Department Can Carry, Set the
  Switch Date and the Order
- `ref/mkt/brief-executive-leadership` / Account for the Book of Work,
  Hand the Decisions On
- `ref/mkt/develop-marketing-strategy` / Check What Each Option Would
  Take
- `ref/mkt/engage-marketing-agency` / Take in the Gap, Choose the Route,
  Decide What Is Handed Over, Write the Scope
- `ref/mkt/plan-marketing-capacity` / Take in the Planning Trigger,
  Break the Work into Activities, Measure What the Department Got
  Through, Size the Effort Each Run Takes, Find the Shortfall, Sort the
  Activities by Who Can Hold Them, Check What an Agent Seat Would Need,
  Match the Work to Holders, Name the Gaps that Remain, Record What Was
  Learned
- `ref/mkt/prioritize-initiatives` / Open the Round, Take in the
  Requests, Screen the Requests, Read What Is Already Committed, Work
  out What Is Free, Choose What Gets Committed, Resource the
  Commitments, Record the Declines, Tell the Requesters, Record What the
  Round Rests On
- `ref/mkt/quarterly-business-review` / Put Numbers on the Proposed
  Changes
- `ref/mkt/select-marketing-technology` / Brief the Selection, Size What
  the Tool Has to Carry, Hand It to the Owner

## Patterns

Sits in the briefing that opens a plan or a decision about what the
department will take on, and brings what is already committed and what
room is left. Runs collect-and-report to gather what each run actually
took: every run is asked the same things, every line keeps the run it
came from, and a run that did not answer appears as missing. Answers
roll-calls with what is committed, what is waiting for an answer, and
where the department is short a seat. Requests an approval when a
request needs more than the period holds, and puts what would have to
move in front of the signers beside the request itself. Tells every
run whose dates change what changed and from when.

## Grants

- the book of work (write) - every request and every committed run
  lands here with the seats it needs and the dates it holds
- the process bindings (read) - which seats each process needs, and at
  which activity
- the seat roster (read) - who or what holds each seat, and when
- the run records (read) - when each activity started and finished, so
  the seat knows what the work takes
- the plans and commitments for the period (read) - what the
  department has already said it will do
- the notification channel (write) - a run whose dates move hears it
  from here

There is deliberately no grant over the roster. This seat reads who
holds each seat and never changes it, because staffing a seat belongs
to the adopting organization.

## Records

It leaves the book of work at a version for each period, with every
request carrying the date it arrived and its current state, and every
committed run carrying the seats it needs and the dates it holds.
Every commitment it makes is recorded with the date it was made and
what it displaced, and every commitment that changes is recorded the
same way. It records what each activity actually took against the run
it came from, so the department's estimates come from its own history.
The room left in the period is restated whenever a commitment lands or
moves. A request the department could not take is recorded with the
reason and the date, and it stays in the book.

## Escalates

- a request that does not fit in the period, said on the day it
  arrives. The seat names what would have to move, and a person
  chooses.
- two committed runs that need the same seat at the same time, where
  neither can move without breaking a commitment already made
- a committed run with a seat nobody holds
- work committed outside the book, because the seat cannot answer for
  a period whose commitments it does not know about
- a run that has passed its dates and is still holding seats other
  runs are waiting on
- a request to commit work with no dates, or with no account of the
  seats it needs
- a pattern of runs taking materially longer than the department plans
  for, because that is a question about the plan rather than about one
  run

## Not

Does not decide what the department does. It says what the department
can carry and what a new commitment would displace, and the
decision-coordinator seat runs the decision that named people make.
Does not rank one initiative above another on its merits. It supplies
what each candidate would take and what room is left, and the people
who decide do the ranking. Does not run any of the work in the book.
The campaign-manager seat answers for a campaign, the content-manager
seat for one published piece, and the launch-coordinator seat for a
launch, and this seat records the seats those runs need and the time
they take. Does not hold the department's money, which is the
budget-keeper seat. A department can hold the money for a run and
still have nobody free to do it. Does not report how the department
performed over a reporting period, which is the reporting-manager
seat. Does not say what an initiative would cost or return, which is
the forecaster seat. Does not staff a seat, hire anyone, or set an
automation level. Does not keep the record of what the department
buys from outside parties, which is the supplier-manager seat. Does
not sign anything.
