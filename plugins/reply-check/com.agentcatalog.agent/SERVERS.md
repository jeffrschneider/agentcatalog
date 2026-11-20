# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each check's result with the sentence and the rule it found, each hold naming the person who must send the reply, what each held reply commits the company to, and each saved reply's mark for approval, with no right to approve, change or send a reply. |
| the knowledge base | read | The approved content each reply cites, at its version. |
| the policy library | read | `<your reply rules>` at their version, with the categories a named person must send and the person each category names. |
| the CRM | read | The facts on the account a reply relies on. |
| the billing system | read | The facts of a bill a reply states, with no right to change a charge, an invoice or a payment. |
| the incident record | read | Engineering's review an outage summary is checked against. |
| the restricted record | read | What the security lead or the safety owner agreed may be said to a reporter. |
| the notification channel | write | Each held reply sent to the named person who must send it and the specialist told, a legal matter sent to `<your legal team>` the same day, and a reporter's question sent to Marketing's press work. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
