# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the calendar | write | The diary has to hold the meeting, not a note about it. |
| the mail system | write | The times, the invitation and the reminders. |
| the meeting tool | write | The joining details travel in the invitation and again in the reminder. |
| the CRM | write | The booking, the write-up and the next step against the account. |
| the recording store | write | Only for a meeting everybody present was told about and agreed to. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
