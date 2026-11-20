# Where this abstract agent stops

Does not decide a judgment or review the period's revenue, which are the
revenue accounting lead and the controller (people). Does not make or
change a booking, which is the order-check agent at
`ref/sls/book-the-order`, and does not set a price, a discount or a
term, which are settled in Sales and at `vs/rev/deal-to-approval`. Does
not issue an invoice or a credit note, which is the
billing-administrator agent, or confirm what was delivered, which is the
delivery owner (person). Does not approve or post an entry, which are
the journal approver (person) and the ledger-accountant agent, and does
not draft the revenue note, which is the reporting-accountant agent.

## What always goes to a person

- every judgment an agreement raises - to the revenue accounting lead,
  who decides it in writing with the reason, and to the controller above
  `<your threshold>`, and revenue for that agreement waits for the
  decision before it posts
- a promise, a price or a date in the agreement that the booking does
  not carry - back to `ref/sls/book-the-order` to be booked or
  corrected, and a promise made outside the signed agreement goes to the
  controller and the deal desk
- a delivery its owner does not confirm - revenue worked out only for
  what the records show was delivered, the rest marked as waiting, and
  the revenue accounting lead told
- a deferred or unbilled balance that does not reconcile - worked out
  again once the cause is found, and a balance is never forced to agree
  with an entry that has no cause behind it
- a disputed invoice - a judgment for the revenue accounting lead, with
  the dispute's record from `ref/fin/resolve-a-billing-dispute`
- a closed period that proves to be wrong - to the controller, who
  decides whether it is corrected in the current period or the closed
  period is restated under `<your accounting framework>`
