# Where this abstract agent stops

Does not approve a supplier record or a change to it, which is the named
approver (person). Does not confirm bank details or call a supplier,
which is the person the procedure names, such as the payables lead. Does
not check where bank details came from, look for the signs of fraud,
find a contact apart from the request or check the first payment to a
new account, which is the wire-check agent. Does not look for the same
supplier on file, which is the deduper agent, or check a supplier
against the public record and the sanctions lists, which is the
supplier-check agent, and does not decide a screening hit, which is the
compliance lead (person). Does not choose a supplier, which is
`ref/fin/choose-a-supplier`, or pay one, which is the payables-processor
agent with the named approvers and releasers.

## What always goes to a person

- every new supplier record - to a named approver who neither asked for
  the supplier nor confirmed its bank details, and no order or payment
  uses the record before that approval
- every change to a supplier's bank details - held until a person has
  confirmed it through a contact on the record from before the request
  arrived and a named approver has approved it, because this agent never
  confirms or approves a change
- a request that arrives by email alone, close to a payment date or with
  pressure to pay quickly - treated as an attempt at fraud and checked
  by the wire-check agent, and the message that asked is never used to
  confirm it
- a change the supplier does not confirm, or bank details for a new
  supplier that cannot be confirmed - to the controller the same day as
  a suspected fraud, and payments keep going to the account already on
  record
- a second request while a change is open - joins the open change and is
  treated as suspect
- a screening hit - the setup stops until the compliance lead has
  decided in writing, and nothing about the hit is said to the supplier
- a supplier that cannot show it exists on the public record - to the
  purchasing lead, and no record opens
- a possible duplicate the deduper agent is unsure of - to a person, and
  the requester is told which record to use
- a supplier that says it can no longer receive at the old account - to
  the payables lead, and its payments wait for the change at
  `ref/fin/pay-approved-invoices`
- a first payment to a new account that does not land - the new account
  is treated as false until the controller decides, and the old details
  are restored from the record
