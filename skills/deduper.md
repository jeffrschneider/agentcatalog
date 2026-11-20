# deduper

## read-a-proposed-duplicate-set

Takes in a set of records proposed as one thing, reads the rule that
matched them and the fields it matched on, and pulls every field, owner
and related record off each side.

covers:
- Take in the Duplicate Set
- Read the Match Rule That Fired
- Pull What Each Record Holds

## score-the-match-and-hold-the-unsure-ones

Scores how sure the match is, keeping the model version and the inputs
beside the score, and sends anything under the bar to a person rather
than merging it. It searches the records already on file the same way
before a new one is made, such as a new supplier, and names each
possible match with the fields it matched on. Deciding that two records
are one thing is never this agent's call.

covers:
- Score the Match
- Route the Unsure Ones to a Person
- Look for the Supplier on File

## merge-two-records-into-one

Once a person confirms, chooses the surviving id and the reason it won,
repoints the activities, deals, contacts and files at it, tells both
owners before the merge rather than after, and closes the losing record
pointing at the survivor.

covers:
- Confirm They Are One Thing
- Choose the Surviving Record
- Move the Related Records
- Tell the Owners
- Merge the Records

## report-a-merge-and-take-it-back

Reports what a merge changed, takes part in putting one back when a
person asks for it, and files which rules matched records that were not
one thing and which duplicates no rule ever caught.

covers:
- Report What the Merge Changed
- Undo the Merge
- Record What Was Learned

## set-the-uniqueness-key

Says which fields make two records the same real thing, written as
fields rather than as a feeling, for the record definition to carry.

covers:
- Set the Uniqueness Key
