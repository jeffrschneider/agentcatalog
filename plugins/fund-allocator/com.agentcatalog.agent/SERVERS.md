# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the fund record | write | Allocations, commitments and releases live here, and this agent is the only thing that moves the balance. |
| the ledger | write | The signed amounts are opened on the books where claims are paid from. |
| the partner record | read | The tier and the standing the rule reads. |
| the agreement record | read | No money is committed against an agreement that expires before the activity date. |
| the partner portal | write | The rule, the eligible activity list and the deadlines are published where every partner can read them. |
| analytics | read | What each partner delivered, which the rule turns into an amount. |
| the CRM | read |  |
| the notification channel | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
