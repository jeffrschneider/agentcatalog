# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the leave management system | write | Each request, its kind and dates, the check against the rules, the approver's decision, the tracking and the balance. |
| the restricted leave file | write | Every document with health information, open only to the named people who must see it, with every opening logged. |
| the HR system | write | The dates taken and the leave balance left at the close, with nothing about the reason for the leave. |
| the accommodation record | read | The decision on a request whose change is time away or reduced hours, without the documents behind it. |
| the notification channel | write | The acknowledgment and each request for a document reach the employee, the dates reach the manager, and an opening of the restricted file by anyone outside the named people reaches the person the policy names. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
