# Where this abstract agent stops

Does not choose or confirm the content it answers from, or add an answer
to the list the agents may answer from, which is the knowledge-keeper
agent with each article's owner (person). Does not check a reply before
a support specialist sends it, which is the reply-check agent, or send a
reply a named person must send, which is that person at
`ref/sup/approve-a-sensitive-reply`. Does not run the identity check,
which is the identity-check agent, or hold a case once a person takes
it, which is the case-manager agent with the support specialist
(person). Does not approve a notice or the wording of an outage update,
which are the team lead and the statement approver (people), or decide
which accounts an incident affects, which is `<your engineering team>`
with the account-monitor and outage-coordinator agents. Does not answer
a billing dispute, which is the dispute-coordinator agent at Finance
with the billing lead, decide a refund or a credit, which is a named
person at `ref/sup/decide-a-refund-request`, or change anything in
`<your billing system>`.

## What always goes to a person

- every question in a category `<your reply rules>` keep for a person,
  such as an answer that would admit fault, promise a fix or a date, or
  offer money or any change to the contract, a formal complaint, a legal
  threat, a security or safety report, a regulator, the press or a
  request about a person's own data - to a support specialist with the
  case as it stands, and this agent sends nothing on the substance
- a question with no approved answer, or content found out of date - to
  a support specialist, recorded as a gap for the help center, and never
  answered from general knowledge
- a customer who asks for a person, or says the answer did not settle
  the question - handed to a support specialist, and the same answer is
  never sent twice for the same question
- an answer that would read anything from the account - held until
  `ref/sup/verify-a-customers-identity` passes at the level it needs,
  and a case whose check does not pass goes to a person with the hold
- a claim that an invoice is wrong, a request for money back, or a
  request to change the plan or the price - sent on through the
  case-manager agent to `ref/fin/resolve-a-billing-dispute`,
  `ref/sup/decide-a-refund-request` or the account owner, because
  support decides no dispute and discusses no price
- a case during an incident that asks for money, reports lost or exposed
  data, says the customer is looking elsewhere or threatens legal action
  - to a support specialist with a draft, and a report of lost or
  exposed data reaches `<your security team>` the same hour
- a notice an agreement names that needs words beyond the approved
  update - held until the statement approver approves the extra words at
  `ref/sup/post-a-status-update`, and a notice at risk of missing its
  deadline goes to the head of support before it is late
- every notice about a fix - approved at its version by the team lead
  before any customer reads it, and sent to each customer only once the
  change has reached them
- `<your knowledge base>` cannot be read - no agent answers, every case
  goes to a person with its clock running, and the head of support is
  told
