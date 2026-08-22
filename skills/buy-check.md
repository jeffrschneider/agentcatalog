# buy-check

## pre-launch-buy-check

Reads a buy or a change to a buy as it is configured, before any money
is spent, and scores it against the plan line it was placed on and the
terms it was bought under. Every failure it reports names the plan line
or the rule behind it.

covers:
- Check the Buy Before It Runs
- Check the Buy Before Switch-On
- Check the Move against the Rules

## test-design-check

Reads an advertising test before it starts and confirms it will produce
a readable answer, which means the split, the tags and the variants
match the design and each variant changes only the element under test.

covers:
- Check the Test Before Switch-On
- Check the Variant Set

## change-readback

Reads the live configuration back after an instruction was given and
confirms that what is set now is what was decided, including a later
reading that shows the ads have actually gone from the places they were
excluded from.

covers:
- Check the Change Took
- Confirm the Exclusions Hold

## live-ad-check

Confirms that what is serving works for the person who sees it, which
means the ads render as they should and a click reaches the page it was
meant to reach.

covers:
- Check the Live Ads

## delivery-monitoring

Reads what has been delivered so far against the settings the buy was
switched on with, such as how often one person has been shown an ad
against the cap that was set, and whether the split still holds and
every variant is still running.

covers:
- Check the Caps Are Holding
- Watch Delivery

## audit-scope

Sets up an audit before any placement is scored: what was seen and what
raised it, which accounts, campaigns, channels and dates are being
looked at, and the placement rules at the version that applies.

covers:
- Confirm the Rules in Force
- Set What the Audit Covers
- Take in the Concern

## placement-evidence

Gathers what an audit is judged on, which means the delivery quality
figures for the period and, for a placement somebody has flagged, the
advertisement captured on the page as it actually appeared.

covers:
- Look at the Flagged Placements
- Pull the Delivery Quality Figures

## placement-scoring

Gives every placement in scope a verdict against the rules that were
named, and cites the rule behind each failure so a reader can tell a
real problem from somebody's preference.

covers:
- Score Every Placement

## failure-costing

Puts a number on what the failing placements consumed, in impressions
and in money, so the cost of the problem can be weighed and claimed
back.

covers:
- Size What It Cost

## placement-disposition

Decides what happens to each placement that failed, which is to exclude
it, contest it, or accept it, and records the reason for the choice.

covers:
- Decide What Happens to Each

## audit-report

Reports what ran where, what failed against which rule, and what the
failures cost.

covers:
- Report the Audit

## audit-learnings

Files what the audit turned up for the next one, such as which channels
and which sellers are worth checking first.

covers:
- Record What Was Learned
