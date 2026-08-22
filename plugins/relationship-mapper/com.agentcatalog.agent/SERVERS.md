# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | write | The people, their roles against a decision, and the last contact date. |
| the contact database and the people sources | read | To find the people the record does not hold, inside the run's cap. |
| the email and calendar record | read | Strength is computed from recorded contact, not from opinion. |
| the consent record | read | What may be held about a person. |
| the account map record | write | The map is issued at a version. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
