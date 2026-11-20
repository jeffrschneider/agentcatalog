# purchasing-coordinator

## take-in-a-request

Takes in a request to buy or a purchase that needs a supplier chosen,
and checks the request for a description, a quantity, a price basis, a
budget line and the dates, asking the requester once for everything
missing.

covers:
- Check the Request Is Complete
- Take in the Purchase
- Take in the Request

## check-the-supplier

Checks that the supplier has an approved record and, above the
threshold, a choice behind it or an agreement in force, sends the
request to a choice of supplier or to supplier setup when either is
missing, and hands the chosen supplier on.

covers:
- Ask for a Choice of Supplier
- Ask for a New Supplier
- Check for a Supplier Already Chosen
- Check the Supplier
- Hand the Supplier On

## issue-the-order

Builds the approved request into an order at a version with its terms,
sends it to the supplier through the contact on its record before any
work starts, and records the supplier's acceptance or the change it asks
for.

covers:
- Issue the Order
- Record the Supplier's Acceptance
- Send the Order to the Supplier

## record-what-was-received

Records each delivery the requester confirms against the order, confirms
the receipt when an invoice is matched, lists what was received and not
yet invoiced at each period end, and passes each capital purchase to the
asset register.

covers:
- Confirm What Was Received
- List What Was Received and Not Invoiced
- Record What Was Received
- Take In the Capital Purchases

## close-the-order

Closes the order once it is received in full and its last invoice is
matched, or once it is cancelled, has what is left released from the
budget line, and records what the run taught.

covers:
- Close the Order
- Record What the Run Taught
