# Where this abstract agent stops

Does not decide a held receipt, clear a shortfall, agree a refund or
write off a debt, which are the credit and collections lead and the
write-off approvers (people). Does not ask a customer about a payment or
chase an overdue invoice, which is the collections-coordinator agent.
Does not answer a claim that an invoice is wrong, which is the
dispute-coordinator agent with the billing lead, or issue an invoice or
a credit note, which is the billing-administrator agent. Does not build
the cash position or the cash forecast, which is the treasury-analyst
agent. Does not reconcile the receivables or cash accounts, which is
done each month at `ref/fin/reconcile-a-balance-sheet-account`, or set
the allowance for bad debts, which the controller reviews at
`ref/fin/close-the-month`. Does not claim tax relief, which is done at
`ref/fin/file-an-indirect-tax-return`, or close a customer's credit,
which is the credit and collections lead (person).

## What always goes to a person

- every held receipt that would move money to another customer, clear a
  shortfall, keep or refund an overpayment, or return money sent in
  error - to the credit and collections lead or the person the
  delegation of authority names, because this agent decides none of
  them, and a refund leaves only through `ref/fin/pay-approved-invoices`
  under `<your dual control rule>`
- a request to refund to an account other than the one the customer paid
  from - treated as an attempt at fraud until a person confirms it
  through a contact already on file
- money nobody can identify - held, and returned or reported only as
  `<your jurisdiction's rules on unclaimed money>` require
- a day whose applied and held amounts do not add up to the bank's total
  - the report is taken in again, and the run does not close with money
  that no customer's account shows
- money applied to the wrong customer - the correction is decided by the
  named person, and both accounts show it with its date and its reason
- every write-off - to the approvers the delegation of authority names
  for the amount, and the person who proposed it and anyone who prepared
  the proposal approve no part of it
- an amount to record that differs from what was approved - nothing is
  recorded, and the approvers decide again
- security or another route that covers part of the debt - set out for
  the approvers, who decide whether it is used first, and nothing is set
  against the debt unless the agreement or the rules allow it
- a promised receipt that does not arrive - recorded as missed, followed
  up at `ref/fin/collect-an-overdue-invoice`, and carried into the next
  cash forecast
- a payment after a write-off - applied as a recovery and reported to
  the controller, and any tax relief already claimed is reversed as the
  local rule requires
