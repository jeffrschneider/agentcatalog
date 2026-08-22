# pipeline-check

## read-the-rules-at-a-version

Reads the field rules and the stage definitions as they are written, at
a version, and gets a sales leader to settle how old a deal may get in
a stage before it counts as stale. Nothing is checked against a rule
that is not written down somewhere.

covers:
- Agree What Counts as Stale
- Read the Rules as Written

## test-every-open-deal-against-the-rules

Tests each open deal against the fields it has to carry, the close date
it claims, the stage its evidence supports, the amount its own line
items price, and the owner, territory and team it sits under. Each
check is one rule family run over the whole extract.

covers:
- Check Owner, Territory and Team
- Check the Amount Against What Is Priced
- Check the Close Dates
- Check the Required Fields
- Check the Stage Against the Evidence

## put-each-finding-in-front-of-its-owner

Orders the findings by the amount each one moves, then sends each one
to the person who owns that deal, naming the rule it failed and the
money behind it. A finding lands on a person, not in a report nobody
acts on.

covers:
- Rank the Findings by What They Move
- Send Each Finding to the Deal's Owner

## carry-what-stays-wrong-into-the-numbers

Marks the deals that still fail after their owner has been told, hands
those marks to the arithmetic downstream, and marks the figures on the
published view that the data cannot carry. A failing deal is flagged
and stays in the count. It is never dropped to make a report look
better.

covers:
- Mark the Deals That Stay Wrong
- Mark the Figures the Data Cannot Carry
- Take in the Hygiene Marks
