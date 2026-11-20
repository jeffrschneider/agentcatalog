# Where this abstract agent stops

Does not answer a customer, which is the customer-question-responder
agent for a routine question and a support specialist (person) for
everything else. Does not check who the person asking is, which is the
identity-check agent, or read the account's standing, which is the
account-monitor agent. Does not decide an urgent case, which is the
person on call or the team lead (person), or rule on an outage, which is
the engineer on call in `<your engineering team>` (person) once the
outage-coordinator agent raises it. Does not write or approve a routing
rule, which is the routing-keeper agent with the support operations lead
(person), or build one in `<your support system>`, which is the
tool-administrator agent. Does not build the after-hours rota, which is
the staffing-planner agent. Does not write to a field in `<your CRM>`,
which goes to its owner through Revenue operations.

## What always goes to a person

- a security or safety report, a legal threat or a regulator's letter, a
  sign of an account takeover, and many requests on one symptom - to its
  owner within `<minutes>` and before the request is sorted, whatever
  queue it would otherwise join: `<your security team>`, `<your legal
  team>`, the team lead on shift or `ref/sup/raise-a-suspected-outage`
- an urgent request outside the team's hours - paged to the person on
  call under `<your after-hours rota>`, then to the next person on the
  rota when the page goes unanswered for `<minutes>`, and to the head of
  support when the rota runs out, because no agent decides an urgent
  case or covers one in place of a person
- a sender who matches no account or more than one - held in the general
  queue with no account's details attached, and a support specialist
  asks the customer once what identifies the account
- a request joined to the wrong case - split out by a support specialist
  into a case of its own with its clock running from its arrival, and
  the join counted for the period's review of the routing rules
- a routing rule that misroutes again and again - to the support
  operations lead for `ref/sup/change-a-routing-rule`, because a rule
  changes only there
- a routing change whose replay or first live requests send an urgent
  request to the wrong place - to the person who owns that route and the
  support operations lead, and the tool-administrator agent restores the
  version before
- an account whose plan cannot be read - the case takes the service
  level `<your service level policy>` sets for an unknown plan, marked
  so, and the gap goes to the owner of the record at
  `ref/rev/fix-a-data-quality-failure`
- a request to close an account or cancel a subscription - placed like
  any other request the same day, and never held back or slowed to make
  room for anyone to try to keep the customer
