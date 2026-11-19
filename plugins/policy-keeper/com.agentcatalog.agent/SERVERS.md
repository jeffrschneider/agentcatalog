# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the policy library | write | Every policy and the handbook at versions, each variant with its effective date and the locations it covers, and each old version kept with the dates it applied. |
| the HR system | read | Each person's location, which decides the variant that covers them, and each acknowledgment a person made under their own sign-in. |
| the answer library | write | Each approved answer stored beside the policy version it rests on, and every answer that rests on an old version marked for review. |
| the signature system | trigger | Sends a final text to the named approvers, with no right to approve or sign. |
| the notification channel | write | Each person covered hears what changed and the date to acknowledge it by, and a manager hears of an acknowledgment still open after the days the company sets. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
