# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the price list system | write | A tier's discount takes effect here, on the date the approved round says it does. |
| the finance system | read | The volume and the cost the pricing is computed from. |
| the partner record | read | Which tier a partner holds, and from what date. |
| the agreement record | read | What the signed terms already give a partner, so a tier does not promise it a second time. |
| the partner portal | write | What a tier entitles a partner to has to read the same in the portal as on the price list. |
| the notification channel | write |  |

There is deliberately no grant over the payment system. This agent says
what is owed and a person pays it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
