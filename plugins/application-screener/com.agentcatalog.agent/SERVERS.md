# The systems this abstract agent needs

Two systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the applicant tracking system | write | Each application read only through the screen's view with the withheld details hidden, the must-haves read at the hiring plan's version, and each note and flag written beside the application, with no right to record a decision or send an answer. |
| the notification channel | write | A flagged application reaches the recruiter. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
