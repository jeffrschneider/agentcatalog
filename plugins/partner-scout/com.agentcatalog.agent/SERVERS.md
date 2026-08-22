# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The partners, customers and suppliers already on the books are read before the market is. |
| market sources | read | Cap: reads per day, set by the adopting organization. |
| the partner record | write | Candidates, scores, refusals and silences are kept where the next search will read them. |
| the outreach channel | write | First contact goes out on the approach a person set, and only after the conflict check. |
| the contact record | write | Who replied, who declined, who never answered, and the reason each one gave. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
