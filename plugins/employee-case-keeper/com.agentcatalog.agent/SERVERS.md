# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the employee relations case system | write | Every case, including the case of a performance improvement plan, with its route, its clock and each decision beside the name of the person who made it. |
| the restricted case file | write | The file of each case, open only to the named people on it, with every opening logged. |
| the HR system | read | The employee's job, manager and location, and an approved leave or an accommodation in progress only as the fact that it is open and its dates. |
| the anonymous reporting line | write | Replies to an anonymous concern through its case reference alone. |
| the calendar | write | Hearings, appeals and check-ins, and the reminder on the date an outcome stops counting. |
| the notification channel | write | An acknowledgment, a date about to be missed, a sign of retaliation or an opening of a file by someone not named reaches the right person the same day. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
