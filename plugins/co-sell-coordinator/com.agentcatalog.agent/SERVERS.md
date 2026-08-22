# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the joint plan record | write | One plan across both organizations, every step with an owner and a date, at a version. |
| the CRM | write | The joint deal, the approaches as they happened, and the outcome. |
| the registration record | read | The claim covering the deal, and the date it ends. |
| the agreement record | read | What the agreement allows the two sides to do together. |
| the partner's system | read | Only what the sharing terms allow, at the cap the process sets. |
| the notification channel | write | The plan, the dates and the contact rule, to both sides at once. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
