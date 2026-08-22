# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the partner record | write | The tier each partner holds, the inputs that produced it, and the rules version behind it. |
| the published tier rules | read | At the version in force, with the date they were published. |
| the evidence set | read | The same measures, over the same period, from the same systems, for every partner in scope. |
| the exception register | write | Every departure from the rules, its reason, the person asking, and the date it expires. |
| the partner portal | write | The entitlement a tier carries, and its removal when a relationship ends. |
| the agreement record | read | What the partner was promised at the tier they hold. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
