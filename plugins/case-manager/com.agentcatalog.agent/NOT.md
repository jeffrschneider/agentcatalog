# Where this abstract agent stops

Does not answer a customer or decide what a reply says, which is the
support specialist (person) who holds the case, or the
customer-question-responder agent on a routine question. Does not check
a reply, which is the reply-check agent, or approve or send a sensitive
reply, which is the named approver for its category (person). Does not
run the identity checks, which is the identity-check agent, or decide a
held request, which is the team lead (person). Does not write the
escalation summary, choose the tier or file a bug, which is the
escalation-coordinator agent. Does not work a churn risk or an
expansion, make an offer or discuss a price, which stay with the account
owner in Sales through the risk-watcher and expansion-spotter agents.
Does not decide a billing dispute, which is Finance's dispute process
with the billing lead, or a refund or a credit, which is the named
person at `ref/sup/decide-a-refund-request` or
`ref/sup/offer-a-goodwill-credit`. Does not score a case, which is the
case-reviewer agent, and rates no support specialist.

## What always goes to a person

- a promise about to be missed - raised to the support specialist while
  there is time to keep it and to the team lead once it has passed, and
  the customer hears before the date passes with a new date the
  specialist can keep
- a case that belongs to another process, such as a reproduced fault, a
  claim that an invoice is wrong, a request for money back, a security
  or safety report, a formal complaint, a request about a person's own
  data, a request to close the account or an account signal - opened
  there with the case and the customer's own words, and the case stays
  with its specialist until that process answers
- an identity check that does not pass, or a request held as a possible
  takeover - the case held with nothing in the account read out or
  changed, for the team lead to decide
- a request to cancel - sent the same day to
  `ref/sup/close-a-customer-account`, which takes it to the account
  owner in the customer's own words, and never delayed or made to depend
  on anything
- a case reopened twice - to the team lead, who decides whether it is
  escalated
- a support specialist who is away - to the team lead, who gives the
  case to another named specialist with its history, its promises and
  what the customer was told
- an account signal the account owner has not taken up within `<hours>`
  - to the team lead, who takes it to the person `<your account coverage
  rule>` names in Sales
- a case after an outage that asks for goodwill beyond the agreement,
  says the customer will leave, claims a loss or threatens legal action
  - to `ref/sup/offer-a-goodwill-credit`, to
  `ref/sup/flag-an-account-signal`, or to `<your legal team>` the same
  day
- Finance's promised date on a disputed invoice about to pass - raised
  on the case before it passes, and Finance's process tells the customer
  the new date and the reason
