# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the development plan record | write | Each employee's development plan, its actions with an owner and a date, the feedback an applicant agreed to keep, and the career interest each person wrote. |
| the job framework | read | The jobs, their levels and the career paths between them, which each plan and each opening is read against. |
| the HR system | read | Each employee's job, manager, team and location, with no pay, health, leave or case record. |
| the performance review system | read | The development actions and the objectives agreed at each review conversation. |
| the applicant tracking system | read | Each internal opening and its must-haves, so the people whose plans name that kind of role hear of it. |
| the learning system | read | Each course published at its version, so the people who asked for it hear it is there. |
| the decision record | read | The possible successors and the readiness the leaders agreed at the succession review. |
| the notification channel | write | Each person told of an opening or a course, and a manager told when a person was never released for one. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
