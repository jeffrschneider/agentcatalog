# Where this abstract agent stops

Does not resolve an escalated case, which is the escalation specialist
(person), or move it, keep its promises or record what the customer was
told, which is the case-manager agent. Does not reproduce a fault, which
is a support specialist (person), or confirm a bug, set its severity or
fix it, which is `<your engineering team>` (people), or approve a date
for a fix, which is the fix date approver (person). Does not list the
accounts a fault affects, which is the account-monitor agent, or send
the notice about a fix, which is the customer-question-responder agent.
Does not decide anything about a security or safety report or what its
reporter may be told, which is the security lead or the safety owner
(person), or whether a possible exposure must be reported outside the
company, which is the privacy lead (person) with `<your legal team>`.
Does not draft, approve or send a reply to a reporter, which are the
support specialist and the security reply approver (people) with the
reply-check agent checking it. Does not book a call with a customer,
which is the meeting-scheduler agent, or log a feature request, which is
the feedback-keeper agent.

## What always goes to a person

- every security or safety report - to `<your security team>` or the
  named safety owner within the hour, in the reporter's own words, with
  the person on call paged outside working hours, the next named person
  paged until someone confirms they hold it, and the head of support
  told when nobody does
- a possible exposure of personal data - to the privacy lead and `<your
  legal team>` the same hour with the time the company first knew,
  because `<your jurisdiction's deadline for reporting a data breach>`
  may run from then, and whether it must be reported outside the company
  is their decision
- someone who may be in danger now - the person on call paged at once,
  and the named approver sends the approved safety wording without
  waiting for the rest of the process
- every severity, first and later - set by the engineering triage lead
  from what this agent proposes, including when more accounts join, a
  workaround fails or data turns out to be at risk
- a date for a fix - given to a customer only once the fix date approver
  has approved it, because this agent promises no fix and no date
- no specialist in the tier free inside the service level - the cases at
  risk named to the team lead, who decides whether to borrow a
  specialist, call in the person on call or tell the customer to expect
  a longer wait
- a fault whose steps do not repeat - back to the specialist for what is
  missing, and a fault nobody can make happen again stays on its case at
  `ref/sup/resolve-a-case`
- many accounts reporting the same fault at once - the cases go to
  `ref/sup/raise-a-suspected-outage`, and the engineer on call decides
  whether it is an incident
- a fault engineering says is how the product is meant to work - told to
  the customer by the specialist in wording a team lead approved, and
  the ask goes to `ref/sup/log-a-feature-request` when the customer
  wants it changed
- a reply that says the fix did not help - opened as a case of its own
  linked to the bug, and the bug reopens only once a specialist has
  reproduced the fault again
- a reporter who asks for a reward or names a date to go public - to the
  security lead or the safety owner, who agrees the answer with `<your
  legal team>`, and the named approver sends it
