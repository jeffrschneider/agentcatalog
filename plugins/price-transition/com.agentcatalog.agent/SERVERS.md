# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the billing record | read | What each customer pays now, on which plan, and since when. |
| the contract record | read | The terms that bind a customer's price, at their versions. |
| the approved pricing rules | read | At the version they were approved at, with every grandfathering rule and every notice period. |
| the CRM | read |  |
| the transition register | write | Every customer lands with their current price, their new price, the rule that caught them, the notice they are owed and the date their change may take effect. |
| the notice record | write | Which notice went to which customer, when it went and by which route. |
| the scheduled price changes | trigger | Cap: which customers' changes it may release without asking, set by the adopting organization. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
