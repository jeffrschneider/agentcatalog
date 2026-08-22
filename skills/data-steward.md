# data-steward

## write-what-a-record-must-contain

Takes in a request to define an object, reads who uses it today and what
counts off it, and writes what the object means and what it is not. Then
the fields it carries, the ones a record may not be saved without, the
values each of those takes, and the fields that make two records the
same real thing.

covers:
- Take in the Definition Request
- Read How the Record Is Used Today
- Write What the Object Means
- List the Fields It Carries
- Decide the Required Fields
- Fix the Allowed Values
- Set the Uniqueness Key

## say-where-each-value-comes-from

Says where every field's value comes from, which source wins when two
disagree, and the one system a number is read from. A value a person
typed is left where it is.

covers:
- Say Where Each Field Comes From
- Read the Field Definitions
- Set Which Source Wins
- Leave Typed Values Alone
- Name the Source of Record

## publish-a-definition-at-a-version

Puts the version in front of the object owner with the failing count and
the breakage list attached, publishes it once a person signs, and sets
the date by which the records already failing must be put right. The
version it replaces stays readable at its own number.

covers:
- Sign the Definition
- Publish the Definition
- Set the Backfill Deadline

## settle-a-merge-field-by-field

Once somebody has confirmed two records are one thing, pulls what each
one holds, settles which record survives and which value wins on every
field, and stores what did not survive against the survivor. That store
is the only reason a merge can be taken back at all.

covers:
- Pull What Each Record Holds
- Choose the Surviving Record
- Settle Every Field
- Keep What the Loser Held
- Undo the Merge

## trace-bad-values-back-to-what-wrote-them

Follows failing values back to the form, the import, the link or the
person that wrote them, names who owns that source, and gets a decision
on whether it keeps writing while it is being fixed. Then the source is
put right, the records already wrong are corrected, and the failure
closes. A trail that runs cold closes as unexplained rather than as
fixed.

covers:
- Trace It to Its Source
- Name Who Owns the Source
- Decide Whether to Stop the Flow
- Fix It at the Source
- Correct the Records Already Wrong
- Close the Failure
- Record What Was Learned

## put-a-rule-in-place-and-tighten-it

Puts a rule into the system once the fields behind it hold up, and
changes it when the same thing keeps coming back. A rule that has to be
tightened or amended lands at a new version with the reason written
down.

covers:
- Implement the Rule
- Tighten the Rule
- Amend the Rules from What Recurred

## sweep-the-open-records-against-the-rules

Reads the rules as they are written, pulls the open records, and checks
each one against what is priced, against who owns it and which territory
and team it sits in, and against whether it is a duplicate or a split.
Fixes what the record can fix and marks what stays wrong rather than
quietly passing it.

covers:
- Read the Rules as Written
- Pull the Open Deals
- Check the Amount Against What Is Priced
- Check Owner, Territory and Team
- Find the Duplicates and the Splits
- Fix What the Record Can Fix
- Mark the Deals That Stay Wrong

## put-right-a-record-a-rule-placed-wrong

Works out why a rule sent a record to the wrong place, and puts the
record itself right.

covers:
- Find Why the Rule Sent It Wrong
- Fix the Record

## test-whether-the-data-carries-what-is-being-built

Reads the fields a report, a rule or a clock is about to rest on and
says whether they hold up: how full each one is, where the times come
from, and whether the timestamps can carry the measure being asked of
them.

covers:
- Check the Data Is There
- Read the Fields the Rule Will Use
- Check the Data Holds Up
- Read Where the Times Come From
- Check the Timestamps Hold Up

## fix-the-boundary-a-number-is-cut-at

Fixes the edges a number is cut at, and keeps them fixed. That is what a
measure counts in and out, the cut-off a set of figures is pulled at,
the period a clock runs over, and the slice and the cadence a report is
read on.

covers:
- Set the Boundaries
- Fix the Cut-Off
- Keep the Period
- Choose the Cut and the Cadence

## tie-the-figures-back-to-one-extract

Pulls the open records at the cut-off, converts them to one currency,
reconciles every cut against the extract they came from, and has a
second person check it before anything goes out. Every figure published
has to tie back to the roll-up.

covers:
- Pull the Open Deals at the Cut-Off
- Convert to One Currency
- Reconcile the Cuts Against the Extract
- Have a Second Pair of Eyes Check It
- Check Every Figure Ties to the Roll-Up

## say-who-may-see-which-cut

Decides what each audience sees, sets who may see a report at all, and
checks the cuts going out against that before they go.

covers:
- Decide What Each Audience Sees
- Set Who May See It
- Check Who May See Which Cut

## say-what-changed-and-what-was-left-out

Records a correction as a new version rather than editing the figure
that already went out, and says plainly what an answer left out. A
report can then name the version it was computed under.

covers:
- Record Corrections as New Versions
- Say What Was Left Out

## retire-a-report

Reads what each report costs and what depends on it, freezes it so it
stops moving, and switches off the feeds behind it.

covers:
- Read What Each One Costs
- Find What Depends on Each One
- Freeze the Report
- Switch Off the Feeds
