# price-transition

## change-terms

Records the terms the change runs under before any customer is sorted:
the approved new prices, the grandfathering rules that hold a customer
at an old price, and the notice period each customer is owed.

covers:
- Set the Terms of the Change

## customer-sorting

Goes through the customers a change affects one at a time, works out
what each pays now and what the new prices make them pay, and applies
the rules to say which group the customer falls in and which notice
they are owed. The result is one register and one list per treatment.

covers:
- Build the Notice Lists
- Read the Affected Customers

## notice-service

Sends each customer the notice their agreement requires, by the route
it requires, and keeps the proof that it went. The date it went starts
the waiting time that has to run out before the price may change.

covers:
- Serve the Notice

## change-release

Holds every customer's price change back until the notice they were
owed has been served and its waiting time has run out, then releases
each change on the date that clears it.

covers:
- Move the Served Customers

## transition-outcome

Reads what customers did as the change took effect, such as who
accepted, who left and what new sales did, and reports the result
against what the change was meant to achieve.

covers:
- Report the Transition
- Watch the Transition
