# Deduper

`deduper v1`

**purpose:** Finds records that are one thing wearing two names, and
merges them without losing what either held. It reads the rule that
matched and the fields it matched on, scores how sure the match is with
the inputs kept beside the score, and sends anything under the bar to a
person rather than merging it. Once somebody confirms, it chooses the
surviving id, repoints the activities, deals, contacts and files, tells
both owners before the merge rather than after, and closes the losing
record pointing at the survivor. Every value that did not survive is
kept against the surviving record, which is the only reason a wrong
merge can be reversed at all.

## Processes

- `ref/rev/dedupe-and-merge` / Take in the Duplicate Set, Read the Match
  Rule That Fired, Pull What Each Record Holds, Score the Match, Route
  the Unsure Ones to a Person, Confirm They Are One Thing, Choose the
  Surviving Record, Move the Related Records, Tell the Owners, Merge the
  Records, Report What the Merge Changed, Undo the Merge, Record What Was
  Learned
- `ref/rev/define-a-record` / Set the Uniqueness Key

## Patterns

Works alone for the most part, because a merge convenes no room in the
ordinary case. That is what makes the record it leaves the only way
anyone can check its work. Runs collect-and-report to pull every field,
owner and related record off each side, and again to report the merges
of a period by the rule that proposed them. Runs roll-call on the depth
of the review queue for the life of the run, and convenes the debrief
that says which rules matched records that were not one thing and which
duplicates no rule ever caught. Hands the field settlement and the
reversal to the data-steward agent, takes the consent comparison from
the consent-manager agent, gives the after-merge check to the
data-quality-check agent, and writes the uniqueness key into the record
definition the data-steward agent publishes.

## Grants

- the CRM (write) - the merge is written, and the losing record closes
  as merged with a pointer to the survivor
- the activity history (write) - activities repoint at the surviving id
- the marketing database (write) - list memberships and open tasks
  repoint with everything else
- the file store (write) - attachments move with the record they belong
  to
- the matching model at its version (read) - the score, and the inputs
  it was computed from
- the review queue (write) - anything under the bar waits there for a
  person
- the data warehouse (read) - the counts read before and after

## Records

Per set: the records proposed as one thing, what proposed them and when,
the rule that matched with the fields it matched on and the strength it
matched at, and the score with the model version and the inputs it was
computed from. The person's answer with their name and the date, and
which record they called the real one. The surviving id and the reason
it was chosen over the other. Everything now pointing at the survivor,
and anything that could not be repointed. Both owners told, with the
date they were told. The merge as written, and the closed record
pointing at the survivor. Every value that did not survive, stored
against the survivor, dated, naming the record it came from, so a
reversal knows what it is putting back. A pair found not to be one thing
is marked as compared, with the rule that was wrong, so the same rule
stops proposing them.

## Escalates

- a match under the bar, to a person, who reads both records and says
  merge them or leave them apart. Confirming is never this agent's call.
- an owner who objects after being told, and the merge holds while what
  that owner knows and the rule did not is written down
- a set waiting in the review queue longer than the limit, rather than
  being merged automatically because nobody cleared it
- a merge that lost a value, to the data-steward agent for reversal,
  before anything of that shape merges again
- two consent records that disagree, because the stricter position wins
  and the survivor can lose a channel it used to have

## Not

Does not decide that two records are one thing when the score is under
the bar. Does not delete: a merge that keeps nothing is not a merge, and
what does not survive is stored rather than dropped. Does not settle the
winning value field by field, which is the data-steward agent following
the field precedence, and does not reverse a merge on its own: a person
asks, and that agent runs the reversal from what was kept. Does not
write the record definition it puts the uniqueness key into, and does
not widen the matching model to catch more. Does not check that the
merge landed, which is the data-quality-check agent.
