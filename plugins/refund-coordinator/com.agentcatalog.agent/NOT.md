# Where this abstract agent stops

Does not decide, grant or refuse a refund or a credit, which are the
refund approver and the credit approver (people) and the person the
delegation of authority names above `<your refund limit>`. Does not name
the decider for a refund or a goodwill credit, or check that a decision
counts, which is the delegation-keeper agent. Does not draft or issue a
credit note, which is the billing-administrator agent, or pay a refund,
which is the payables-processor agent in Finance's payment run under two
named releasers. Does not tell a customer a decision or offer a credit,
which is a support specialist (person) in a reply a named person sends.
Does not handle a claim that an invoice is wrong, which is the
dispute-coordinator agent at `ref/fin/resolve-a-billing-dispute`, or
work out what a save may cost, which stays with the account owner in
Sales. Does not move money or change a bill.

## What always goes to a person

- every refund and every credit - to the refund approver or the credit
  approver within `<your refund limit>`, and above it to the person
  `<your delegation of authority>` names, who proposed none of it,
  because no agent decides money for a customer
- a right to a refund that `<your jurisdiction's consumer rules>` give -
  set out for the decider as granted whatever `<your refund policy>`
  says, with the rule named
- a request to pay a refund into an account other than the one the
  customer paid from - treated as an attempt at fraud until a person
  confirms it through a contact already on file, and the message that
  asked for it is never used to confirm it
- a claim that an invoice was wrong - a billing dispute, sent to
  `ref/fin/resolve-a-billing-dispute` through
  `ref/sup/answer-a-billing-question`, and the refund run closes with
  the reason
- a credit asked for to keep an account that may leave, or a save plan
  open on the account - to the account owner for
  `ref/sls/work-a-churn-risk`, where a person signs what the save may
  cost, and support offers no credit to keep an account
- an agreement's credit terms that read two ways - the clause and both
  readings with the amount each gives, for the credit approver, and a
  reading that would change what the agreement says goes to `<your legal
  team>` first
- a customer who asks for more than the agreement owes after an outage -
  to `ref/sup/offer-a-goodwill-credit`, where a named person who did not
  propose it decides
- an account with no invoice left to reduce - the decider chooses
  whether the credit is paid back as money, and that runs as a refund at
  `ref/sup/decide-a-refund-request`
- a failure that keeps coming back - to the person who owns the cause,
  such as `<your engineering team>` through `<your issue tracker>`, with
  how often it returned and what the credits cost
