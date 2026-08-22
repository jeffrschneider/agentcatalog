# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the budget record | write | Each allocation lands at a version with the date it took effect. |
| the commitments already made | read | The agreements, retainers and renewals signed before the money was divided. |
| the order record | read | What has been ordered against each allocation and by whom. |
| the accounting record for the period | read | What has been billed and what has already been paid. |
| the reconciliation record | read | The checked spend figure for a closed period. |
| the supplier record | read | The term and the renewal date on every entry the department pays for. |
| the notification channel | write | Every function is told what it holds and from when. |

There is deliberately no payment grant and no ordering grant. This agent
records money and moves none of it, which is what makes its figures
worth reading.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
