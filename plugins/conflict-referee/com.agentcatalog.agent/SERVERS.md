# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the decision record | write | The decision, the rule version, the facts it turned on, the signer, and the precedent it becomes. |
| the CRM | read | The two deals, their dates and their activity. |
| the registration record | read | Every registration on the customer, with its owner and its end date. |
| the activity record | read | Who contacted the customer, when, and from which side. |
| the partner record | read | The agreement, and the standing of the partner raising the claim. |
| the notification channel | write | The stop, and the one decision text both sides receive. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
