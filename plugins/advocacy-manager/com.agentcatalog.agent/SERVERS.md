# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the advocacy record | write | Every ask, agreement and refusal lands dated. |
| the CRM | read |  |
| the account standing record | read | What the account-monitor agent found about the customer. |
| the rights and permissions record | read | What each customer has already agreed the organization may use. |
| the outreach channel | write | Cap: how often one customer may be asked, set by the adopting organization. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
