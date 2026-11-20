# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| product usage data | read |  |
| the support system | read |  |
| the CRM | read |  |
| contract and renewal records | read |  |
| the account standing record | write | Each answer lands dated, with the evidence under it. |
| the billing system | read | What an account pays and any invoice still open, behind a feature request, a closure and an account signal, with no right to change a charge. |
| the issue tracker | read | What engineering can tell about the accounts a confirmed fault reaches. |
| the incident record | read | The features, regions and plans engineering confirmed an incident affects. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
