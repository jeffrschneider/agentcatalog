# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the identity system | write | Cap: accounts per partner, set by the adopting organization. |
| the partner portal | write | Visibility, published material and the list of who is certified. |
| deal registration | write | A deal is registered against the partner with its protection period. |
| the support desk | write | The partner's route to help opens and closes with the rest of their access. |
| the licensing system | write | What the partner may issue, opened against what the agreement covers. |
| the certification record | read | Nobody is entitled by a certificate they do not hold. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
