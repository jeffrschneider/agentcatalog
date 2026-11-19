# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the evidence log | write | The allegations as questions, the investigation plan, every item of evidence with its source, its date and who gave it, the timeline, and the evidence set out against each allegation. |
| the restricted case file | read | The referral, the concern and the route decision, open to this agent only for the investigation it supports. |
| the systems holding the records under hold | read | The messages, logs and documents the plan names, read only once the HR system administrator has held them. |
| the HR system | read | The job, manager and location of each party and witness, so each interview can be booked in private. |
| the calendar | write | Each interview, booked so that nobody learns who else is seen. |
| the notification channel | write | Each invitation sent to the person alone, and a new allegation or a breach of confidence reaches the investigator the same day. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
