# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the entitlement record | read | What the customer is already entitled to, and when each entitlement ends. |
| the contract record | read | The contract behind every existing entitlement, so nothing is quoted twice. |
| the product rules | read | The dependencies, minimums and conflicts the configuration is tested against. |
| the quoting system | write | The configuration lands there at a version, and the check result lands beside it. |
| the document store | write | The record of what was configured and what the approvals took. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
