# roll-up-builder

## fix-the-moment-the-numbers-are-read-at

Fixes one cut-off, pulls the open deals as they stand at that moment
into one extract, and takes in the hygiene marks, so a deal the record
could not support is counted and flagged rather than quietly dropped.

covers:
- Fix the Cut-Off
- Pull the Open Deals at the Cut-Off
- Take in the Hygiene Marks

## put-every-deal-on-one-footing

Converts every deal to one currency with a rate table that is named,
dated and applied once, and gives every deal the category the written
definition produces, set beside the category the record claimed.

covers:
- Apply the Category Definitions
- Convert to One Currency

## sum-the-deals-along-each-dimension

Sums the same deals along whatever dimensions leadership asks for, and
ties every cut back to the extract deal by deal. A difference is chased
until it is understood, never posted as a rounding line or an other
row.

covers:
- Reconcile the Cuts Against the Extract
- Roll the Deals Up by Each Dimension

## say-what-moved-since-the-last-cycle

Sets this cycle against the last one on the same rules, works out what
moved and why, and attaches that movement to the view when it is
published. Every definition, rate or cut-off change is marked at the
cycle it happened in.

covers:
- Attach What Moved Since Last Time
- Compute What Moved
- Set It Against the Last Cycle

## freeze-the-arithmetic-at-a-version

Writes down the questions this roll-up cannot answer, each with the
reason, then freezes the result at a version pinned to its extract, its
rate table and its definitions.

covers:
- Freeze the Roll-Up at a Version
- Mark What the Roll-Up Cannot Answer

## check-a-published-figure-ties-to-its-version

Carries the frozen version into the published view and checks that
every figure on it rebuilds from the roll-up it claims to come from.

covers:
- Check Every Figure Ties to the Roll-Up
- Take in the Frozen Roll-Up
