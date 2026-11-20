# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the collections tool | write | Each reminder schedule, each reminder and reply, each promise, each account set out for a decision, and each pause and restart, with no right to agree a payment plan, a settlement or a hold. |
| the receivables ledger | read | Each open invoice, its age, the receipts applied and the receipts held. |
| the credit record | read | The follow-up level set for the customer and any hold on its orders. |
| the CRM | read | The account owner and the payables contact on the customer's record. |
| the billing system | read | A copy of each invoice a reminder carries. |
| the verified bank record | read | The company's bank details on each reminder. |
| the dispute register | write | Each claim a customer makes in a reply or with a short payment, logged in the customer's own words. |
| the agency's portal | write | An agency holding a debt told the outcome of each decision as the agency agreement sets, with no right to pass a debt to an agency. |
| the notification channel | write | Each reminder reaches the payables contact on the customer's record, the customer is asked once about each held receipt, and the account owner is brought in at the stage the schedule sets. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
