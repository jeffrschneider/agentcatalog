# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the book of work | write | Every request and every committed run lands here with the agents it needs and the dates it holds. |
| the process bindings | read | Which agents each process needs, and at which activity. |
| the agent roster | read | Who or what holds each role, and when. |
| the run records | read | When each activity started and finished, so the agent knows what the work takes. |
| the plans and commitments for the period | read | What the department has already said it will do. |
| the notification channel | write | A run whose dates move hears it from here. |

There is deliberately no grant over the roster. This agent reads who
holds each role and never changes it, because staffing a role belongs to
the adopting organization.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
