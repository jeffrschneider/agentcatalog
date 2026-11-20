# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each case's owner, its state and its clock, each identity result and hold, each promise with its owner and its date, each link to a bug, an incident, a dispute or another process, each approval and each message the customer was sent, and each close and reopen, with no right to send a reply or to change anything in the account. |
| the CRM | read | The account, its plan, its contacts and the account owner each signal and each request to change the plan or the price goes to. |
| the knowledge base | read | The approved content each reply on a case cited. |
| the billing system | read | The bill a question names, with no right to change a charge, an invoice or a payment. |
| the contract repository | read | The customer's agreement behind a complaint or a billing question. |
| the phone system | read | The call records behind a complaint. |
| the issue tracker | read | The bug each case is linked to and its state. |
| the dispute register | write | Each claim that an invoice is wrong, logged in the customer's own words with the invoice, the line and the amount, with no right to decide it. |
| the notification channel | write | Each promise raised to its specialist before its date and to the team lead once it has passed, each signal not taken up raised with the team lead, and each case handed on told to the process that now holds it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
