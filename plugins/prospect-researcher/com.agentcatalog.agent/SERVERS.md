# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the account data sources | read | The candidate accounts, each one naming where it came from. |
| the contact data sources | read | Inside the run's daily cap. |
| the verification source | read | Every address and number is checked before it is used. |
| the CRM | write | The list, and where every person on it sits. |
| the sending system | write | The signed list lands where the sequences read it, with its consent finding attached. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
