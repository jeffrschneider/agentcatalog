# commission-calculator

## open-a-period-and-freeze-the-bookings

Opens the period with its boundaries and the sellers in scope, and pulls
the bookings once into a snapshot carrying the system, the query and the
timestamp it was taken at. Everything after that runs from the snapshot
rather than from a live read.

covers:
- Open the Period
- Pull the Bookings

## place-every-booking-on-a-seller

Matches each booking to a seller, a territory and the plan version that
seller sits on, checks the record carries the fields a payment depends on,
and applies the credit rules that split an amount. Nothing defaults to
the nearest plausible seller, and an unmatched booking is listed rather
than dropped.

covers:
- Apply the Credit Rules
- Check the Booking Record Is Complete
- Match Each Booking to a Seller

## compute-what-a-seller-earned

Measures attainment against that seller's own quota and computes each
component with the rate and the input stored next to the result. Gates,
accelerators and caps go on in the order the plan sets, each marked
applied or not applied, draws and clawbacks are netted, and anything not
yet payable is held with the condition it waits on.

covers:
- Apply Gates, Accelerators and Caps
- Compute Each Component
- Hold Back What Is Not Yet Payable
- Measure Attainment
- Net Draws and Clawbacks

## show-the-working-and-have-it-read

Builds each statement so that every line names its booking, its rate,
its plan sentence and its date, puts it in front of the manager who has
to stand behind it, and records what they accepted and what they said
was wrong.

covers:
- Have the Manager Read the Statements
- Record the Corrections
- Show the Working, Line by Line

## price-a-draft-plan-on-paper

Runs a draft plan over the awkward deals the business really sells and
says what it would pay for each one. Builds the worked examples the way
the real run will compute them, and hears the published wording at the
same time as the managers who have to explain it.

covers:
- Brief the Managers and the Calculator
- Build the Worked Examples
- Test the Plan Against Awkward Cases

## recompute-a-line-a-claim-disputes

Freezes the statement at the version the claimant holds, pulls the
records the number was computed from, and computes the line again
independently from those same records. Where the claim is upheld, the
correction lands in the next run as its own line and the cause goes back
to whoever owns it.

covers:
- Correct the Statement and the Next Run
- Feed the Cause Back
- Freeze the Statement Version
- Pull the Evidence Behind the Line
- Recompute the Line Independently
