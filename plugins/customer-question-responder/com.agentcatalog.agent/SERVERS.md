# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the knowledge base | read | The approved content on the list the agents may answer from, at its version, with no right to change an article or to add one to the list. |
| the support system | write | Each answer, draft, notice and update on its case with the content and the record it rests on, each case handed to a person with the reason, and each customer recorded as told, with no right to send a reply on a case a person holds. |
| the CRM | read | Only the parts of the customer's record an answer needs, such as the plan, a setting or the state of an order, and the contacts each notice goes to. |
| the billing system | read | The invoice, the charge or the payment a billing question names, with no right to change a charge, an invoice or a payment. |
| the contract repository | read | The billing terms of the agreement at its version. |
| the issue tracker | write | Each customer told about a fix recorded on the bug or the request, with no right to change its state or its severity. |
| the policy library | read | `<your reply rules>` and `<your incident policy>` at their versions, and `<your jurisdiction's rule on telling a customer it is dealing with an agent>` where it applies. |
| the outbound mail system | write | Each notice an agreement names, sent to the contact it names by the route it names, and the approved update sent to the other affected accounts. |
| the notification channel | write | Each case handed to a support specialist, and each customer told in the approved words when a person will reply. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
