# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the plan record | write | Every plan at a version, with its cost model and its worked examples kept beside it. |
| the quota record | read | The quota each seller carries. |
| the CRM | read | The deal shapes the business actually sells, so the awkward cases are real ones. |
| the payroll system | read | What last period's plans actually paid, seller by seller. |
| the document store | write | The wording as published, with every earlier version left readable. |
| the signature system | trigger | The plan goes to its named signers and comes back signed at a version. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
