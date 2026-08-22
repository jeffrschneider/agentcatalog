# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the sending system | write | Inside a daily send cap. |
| the phone system | write | The calls due on the day they are due. |
| the social channels | write | Inside the weekly limit for one person. |
| the suppression list | write | A person who says stop is suppressed on every channel, not only the one they said it on. |
| the consent record | read | No touch goes out that it does not cover. |
| the CRM | write | Every touch and every reply against the person. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
