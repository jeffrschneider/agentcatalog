# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the standards store | write | Each standard lands at a numbered version, and an issued version is never edited. |
| the interpretation record | write | What a rule means, attached to the rule and the version it interprets. |
| the notification channel | write | Every agent that reads a standard is told what changed and from when. |
| the approval record | read | The sign-off that has to pass before a change becomes a version. |
| the process bindings | read | Which processes read which standard. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
