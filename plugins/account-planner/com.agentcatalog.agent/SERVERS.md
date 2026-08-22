# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the plan record | write | The plan is issued at a version, and a version it replaces stays where it is. |
| the account read record | write | It assembles and issues the read. |
| the account map record | read | Every opportunity names a buyer from the map, or is marked as having none. |
| the CRM | read | The history, the open deals and who owns the account. |
| the pricing record and the offer catalogue | read | To say what could be sold and roughly what it is worth. |
| public and paid research sources | read | Inside the run's spend cap. |
| the notification channel | write | Everyone who acts on the plan is told what they were given and when it applies from. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
