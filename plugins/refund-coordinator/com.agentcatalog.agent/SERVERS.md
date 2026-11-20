# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the support system | write | Each request taken in from its case in the customer's own words, and the proposal, the decision and the payment run noted on the case, with no right to send a reply that offers money. |
| the billing system | read | Each order's invoice, the payment, how the customer paid, and the refunds and credits already given, with no right to change a bill or issue a credit note. |
| the order system | read | The order or the charge a refund is asked for. |
| the contract repository | read | Each agreement's terms on refunds and on the credits it owes for an outage. |
| the policy library | read | `<your refund policy>` at its version, with its goodwill part, read for each request and each credit. |
| the CRM | read | The account a credit is asked for and its account owner. |
| the incident record | read | The downtime engineering's review measured for each affected account. |
| the delegation of authority | read | Who may decide each outage credit for its amount. |
| the refund register | write | Each request, each proposal at its version with everyone who proposed it, each decision with who made it and under which version of the delegation, the credit note and the payment run, with no right to record a decision of its own. |
| the notification channel | write | The support specialist and the account owner asked what they know, each refund passed to Finance's payment run as an approved item, each decided outage credit passed to Finance, and each cause sent to the person who owns it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
