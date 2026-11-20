# expense-check

## check-against-the-policy

Takes in each claim, and sets every line and every card transaction
against its receipt, its business reason and the limit for its kind,
returning each as inside the policy, outside it with the rule it breaks,
or missing its evidence.

covers:
- Check Each Line Against the Policy
- Check Each Transaction Against the Policy
- Take In the Claim

## find-spend-claimed-before

Sets each line or transaction against the claims already made, the card
transactions and the travel bookings in the expense record, and names
any earlier one it repeats.

covers:
- Check for Spend Claimed Before

## mark-the-part-treated-as-pay

Marks each line the local rules treat as pay, such as an allowance above
the rate those rules allow, with the part treated as pay.

covers:
- Mark the Part Treated as Pay

## follow-up-with-the-employee

Asks the employee for each missing receipt or reason, or about a line
that repeats earlier spend, and records what each claim taught.

covers:
- Ask the Employee About a Line
- Record What the Claim Taught
