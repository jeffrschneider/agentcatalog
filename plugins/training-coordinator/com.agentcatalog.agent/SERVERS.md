# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the learning system | write | Each assignment at its course version with its due date, and each booking, exemption, reminder, chase and completion, which together are the record auditors read. |
| the HR system | read | Each person's role, location and manager, which decide what they must take, and nothing else about them. |
| the course library | read | Each course at the version its owner signed, which is the only version assigned. |
| the calendar | write | The live sessions and the year's sessions, booked in working time with the trainer and the room or the link. |
| the notification channel | write | Reminders and chases reach each person and then the manager, and anyone who stays overdue reaches the department head. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
