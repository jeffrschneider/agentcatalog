# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the territory map | read | The patches it is putting numbers on. |
| the reporting warehouse | read | What each patch closed before. |
| the pay plan record | read | What the plan pays at each case. |
| the quota record | write | The drafts, the signed set, the versions. |
| the notification channel | write | Every seller sees their own statement on one date. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
