# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the document store | read | The signed agreement says what the partner may sell, deliver and earn. |
| the partner record | write | The named people, the plan and the dates land here. |
| the partner portal | write | The materials set is published at a version and republished rather than edited in place. |
| the CRM | write | Deal registration is set up against what the agreement allows. |
| the calendar | write | The kick-off and the plan dates are booked on both sides. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
