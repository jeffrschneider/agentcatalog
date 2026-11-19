# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the applicant tracking system | write | The hiring plan at its version, every application with its source, the withheld details, the notes, the scorecards, each decision and each answer. |
| the HR system | read | The approved position and, for an internal move, the applicant's current role and manager. |
| the careers page | write | Each approved version published and taken down, with its dates. |
| the internal job board | write | The opening shown to employees as the internal posting policy sets. |
| the job boards the hiring plan names | write | Each approved version published and taken down. |
| the calendar | read | Whether each interviewer is free on the planned dates. |
| the training record | read | Whether each interviewer has the interview training the policy requires. |
| the consent record | read | Which applicants agreed to be kept on file, and until when. |
| the notification channel | write | Each acknowledgment and answer reaches the applicant, a late scorecard reaches its interviewer, and a date at risk reaches the recruiter. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
