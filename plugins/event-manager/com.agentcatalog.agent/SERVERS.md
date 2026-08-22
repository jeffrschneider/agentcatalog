# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the event plan and its schedule | write | What each agent owes and when it is due. |
| the invitation and attendance record | write | Who was invited, who registered, who came. |
| the orders placed for the event | read | What has been committed and what it cost. |
| the CRM | read |  |
| analytics | read |  |
| the asset store | read |  |
| the notification channel | write | A call made on the day reaches every agent working the event. |

There is deliberately no ordering grant. This agent says what the event
needs and by when, and the event-operations agent places the orders
inside the limits a person set.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
