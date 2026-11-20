# Where this abstract agent stops

Does not approve an invoice exception or a payment run, or release a
payment, which are the invoice approver, the payment approver and the
two releasers (people). Does not check the payment file against the
verified bank record or confirm where each payment landed, which is the
wire-check agent. Does not name the approver for an exception, which is
the delegation-keeper agent, or confirm what was received, which is the
purchasing-coordinator agent with the requester. Does not change a
supplier's bank details, which is
`ref/fin/change-a-suppliers-bank-details`, or an employee's, which is
`ref/hr/change-an-employee-record`. Does not check an expense claim
against the policy, which is the expense-check agent, or decide what
waits when cash is short, which is the treasurer (person). Does not run
payroll, which is the payroll-administrator agent. Does not change an
amount a supplier billed.

## What always goes to a person

- every payment run - to a named approver who prepared none of it, and
  then to two named people who release the payments under `<your dual
  control rule>`, because this agent never releases money or holds the
  access to do so
- an invoice that does not match its order and receipt, has no order, or
  comes from a supplier with no approved record - to the approver the
  delegation of authority names, who is neither the requester nor
  whoever confirmed the receipt, and an invoice with no approved record
  waits for `ref/fin/set-up-a-supplier`
- a possible duplicate - held beside the invoice it may repeat for the
  payables lead to decide, and a pattern of them from one supplier is
  raised with that supplier
- bank details on an invoice that differ from the supplier's record -
  paid only to the record, and the difference starts
  `ref/fin/change-a-suppliers-bank-details`
- a pattern of invoices with no order from one department - to the
  purchasing lead, because the order is the first control on what the
  company spends
- a run the cash will not cover - to the treasurer, who funds the paying
  account or chooses which items wait, and no agent decides which
  supplier waits
- an early-payment discount whose date falls before the payment date -
  proposed in the last run before it, and the treasurer decides whether
  the discount is worth the cash leaving early
- an urgent payment outside the payment calendar - a run of its own with
  the same checks, the same approval and the same releasers, and a
  pattern of them goes to the payables lead, because urgency is a common
  cover for fraud
- a payment returned or rejected - held aside and paid again only to
  verified details in a run a named approver has approved, and an
  employee's account changed by email alone is treated as an attempt at
  fraud until `ref/hr/change-an-employee-record` confirms it
