# territory-modeler

## fix-the-rule-a-carve-is-drawn-on

Takes in how many territories are wanted and the shape they should have,
and fixes what a territory is cut on before anything is drawn. A rule
changed after the maps exist voids them, and the draw runs again.

covers:
- Take in the Number and the Shape
- Fix What a Territory Is Cut On

## draw-the-candidate-maps

Draws candidate cuts on that rule with every account placed exactly
once, and fixes the one a named person chooses, carrying its version,
the rule it was drawn on and the date it takes effect. The maps that
lost are kept, each with the reason it lost.

covers:
- Draw the Candidate Cuts
- Fix the Territory Map

## say-what-a-patch-can-carry

Models what each patch can carry against what it closed before, and
reads that history again when the numbers are being set. Beside every
carrying number sits the assumption it rests on and what would make that
assumption wrong. A number that cannot name its source is marked
unsourced where a reader sees it.

covers:
- Model What Each Patch Carries
- Read What Each Patch Carried
- Record What the Model Rests On

## hand-the-map-to-quota-setting

Hands the fixed map and its carrying numbers to whoever puts a number on
each patch, and stands behind the map while that work runs.

covers:
- Hand the Map to Quota Setting
- Take in the Map and the Number

## move-an-account-between-patches

Takes in a request to move an account, finds the line of the carve that
allows it, and records the move against the carve. An account the rule
is silent about goes to whoever amends the rule instead.

covers:
- Take in the Request
- Find the Rule That Allows It
- Record the Move Against the Carve

## answer-an-appeal-against-the-carve

Takes the approved carve, builds each seller the statement of what they
hold, tests every appeal against what is written down rather than
against who is asking, and applies what changed.

covers:
- Take in the Approved Carve
- Build a Statement per Seller
- Test Each Appeal Against the Record
- Apply What Changed
