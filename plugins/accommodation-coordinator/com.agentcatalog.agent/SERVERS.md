# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the accommodation record | write | Each request, its dates, the options, the decision with the person who made it, and the review date. |
| the restricted file | write | Any health detail and the information the decision needs, held apart from the employee's record and open only to the named people on the request, with every opening logged. |
| the HR system | read | The employee's job, manager and location, which shape the options. |
| the calendar | write | The conversation and each review date. |
| the notification channel | write | The acknowledgment and the written decision reach the employee, and the teams that make a change hear what to change and nothing about why. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
