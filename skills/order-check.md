# order-check

## read-the-paper-into-a-booking

Lifts the terms out of the executed agreement into fields, each field
naming the clause it came from, and sets the start, end, notice and
renewal dates against the clause that fixed each one. A date the paper
leaves open is named as open rather than guessed.

covers:
- Read the Terms into a Booking
- Set the Term and the Dates

## test-the-booking-against-the-record

Prices every line at a price book version or names the approval that
let it differ, matches every sold line to something that exists and to
a date the delivery side can meet, and scores the whole booking against
the booking rules at a version. A booking that fails goes back to be
corrected.

covers:
- Check What Was Sold Against What Exists
- Price the Booking
- Score the Booking

## get-the-booking-approved

Puts the booking in front of the finance approver at a version and
records who signed it and when. A booking that changes afterwards goes
back through approval, because the approval covered a version.

covers:
- Get Finance Approval

## write-the-booking-where-it-is-acted-on

Writes the approved booking into the order system, passes the billing
schedule, the payment terms and the purchase order reference to
finance, and closes the opportunity at the amount actually booked
rather than the amount forecast.

covers:
- Close the Opportunity
- Pass the Billing Terms to Finance
- Record the Booking

## check-the-handover-package

Takes the booked order in and scores the handover package against its
checklist at a version, naming what is missing rather than what is
present. A gap is carried forward with a date rather than waived
quietly.

covers:
- Check the Package Is Complete
- Take in the Booked Order
