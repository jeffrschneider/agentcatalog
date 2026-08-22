# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the tool | write | Accounts, roles and configuration are this agent's standing work. |
| the account record | write | Every account with the role it holds and the person who approved it. |
| the configuration record | write | Each change with its date, its version, the request behind it and the way back. |
| the identity system | read | Joiners and leavers, so an account is opened against a job and closed against a leaving record. |
| a non-live environment | write | No change is made straight to live where a copy exists. |
| the flow record | read | What the links either side carry, and when each was last checked. |
| the stack record | read | The entry, the licence, the term and the process the tool runs. |
| the budget record | read | What the sellers cost, read against what is actually used. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
