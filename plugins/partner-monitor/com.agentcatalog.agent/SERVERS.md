# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The deals a partner registered and what became of them. |
| the deal registration system | read | What the partner brought, and when. |
| the agreement record | read | What each side owes, at the version that was signed. |
| the training record | read | Who is certified, on what, and until when. |
| the finance system | read | What was earned, what was claimed and what was paid. |
| analytics | read | Both sides read the same measures from one place. |
| the partner record | write | Each reading lands against the partner, dated. |
| the commitment tracker | write | What each side committed to, and whether it happened. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
