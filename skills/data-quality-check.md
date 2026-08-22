# data-quality-check

## write-the-rules-a-record-is-held-to

Writes what the system refuses at save time, what it warns on and what
it only reports later, holds that split at a version, runs it over the
records already held to see what would fail, and turns it on with the
failing count read on a cadence afterwards.

covers:
- Write the Rules That Enforce It
- Test the Rules on Real Records
- Turn the Rules On

## run-the-rules-over-what-something-just-wrote

Runs the definition's rules over everything an enrichment wrote and
holds back the fills that fall under the bar. Reads the record counts,
the related record counts and the affected reports before and after a
merge, and says what did not move.

covers:
- Run the Rules Over the Fill
- Hold Back the Weak Fills
- Check the Merge Landed

## confirm-a-failure-and-find-what-wrote-it

Takes in a failing rule and re-runs it to see whether the failure is in
the data or in the query behind it. Then measures how far it spread,
finds the day it started, and traces it back to the form, the import,
the link or the person that wrote the bad values.

covers:
- Take in the Failing Rule
- Check the Failure Is Real
- Measure How Far It Spread
- Trace It to Its Source

## prove-the-fix-held

Runs the rule again only after the source has been fixed, reads it on
its cadence across a watch period, and tightens it where the failure
showed the rule was too loose. Records still failing go back to the
trace, because there was more than one source.

covers:
- Run the Rule Again
- Watch That the Fix Held
- Tighten the Rule
