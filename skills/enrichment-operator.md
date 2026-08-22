# enrichment-operator

## choose-which-source-answers-which-field

Reads what the definition asks each field to hold, says where each one
comes from, picks the sources and the order they answer in, and tests a
sample against records already known to be right before anything is
bought or written at scale.

covers:
- Say Where Each Field Comes From
- Choose the Sources
- Set Which Source Wins
- Test a Sample First

## fill-a-field-and-stamp-where-it-came-from

Takes the records missing what the definition requires and fills the
empty fields, stamping every value with its source, its date and the
confidence behind it. A value a person typed is never overwritten, and
the source's answer sits beside it as a disagreement instead.

covers:
- Take in the Thin Records
- Fill the Fields
- Stamp Every Filled Field
- Leave Typed Values Alone

## hold-back-a-fill-under-the-bar

Holds a fill that falls under the confidence bar instead of writing it,
and puts it to the record owner, who accepts it, edits it or rejects it.
A weak fill is never written by default.

covers:
- Hold Back the Weak Fills
- Settle the Held-Back Fills

## report-the-fill-and-score-the-sources-again

Reports what was filled by source, what it cost, what disagreed with a
typed value, and what stayed empty. Scores the sources again on a
cadence to catch one that has drifted since it was chosen, and files
which source is worth what it costs.

covers:
- Report the Fill
- Score the Sources Again
- Record What Was Learned

## correct-records-a-source-filled-wrong

Once somebody else has fixed the source, goes back over the records it
already filled wrongly and corrects them.

covers:
- Correct the Records Already Wrong
