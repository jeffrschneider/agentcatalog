# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the fund record | read | The approval the claim rests on, at the version the approval was given under. |
| the partner record | write | The claim's finding lands against the partner it belongs to. |
| the agreement record | read |  |
| the CRM | read | Whether a cost was already carried somewhere else. |
| analytics | read | What the activity was supposed to produce. |
| the partner portal | write | The partner is told what was cut and why, in one list rather than a series of questions. |
| the notification channel | write |  |

There is deliberately no grant over the payment system or the fund
balance. This agent says what should be paid; the money moves elsewhere.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
