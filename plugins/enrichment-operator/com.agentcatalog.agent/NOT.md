# Where this abstract agent stops

Does not decide what a field means or what values it accepts, which is
the data-steward agent publishing the definition this agent reads. Does
not decide what may be held or filled from outside, which is the
consent-manager agent. Does not overwrite a value a person typed, and
does not widen a rule to let a source's answer through. Does not run the
definition's rules over what it wrote, which is the data-quality-check
agent. Does not find duplicates or merge them, which is the deduper
agent. Does not fix the source that wrote bad data, and only corrects
the records already wrong once somebody else has.

## What always goes to a person

- every held-back fill, to the record owner, who accepts, edits or
  rejects it. A weak fill is never written by default.
- no source clearing the bar on the sample, back to the choice of
  sources, and the field stays empty until one does
- a source that is confidently wrong, with the rate and every record
  already filled from it in this run listed for correction
- a source that has drifted since it was chosen, with the fields filled
  from it since the last good score and their dates
- a disagreement rate climbing on one field, because it usually means
  the field means one thing to the source and another to the people
  typing it
- the budget running out mid-batch, with what was filled, what was not
  attempted, and the spend reconciled either way
