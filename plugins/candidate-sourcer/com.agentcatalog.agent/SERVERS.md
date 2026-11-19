# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the applicant tracking system | write | Each person who said yes added as a candidate with their source and their agreement to be considered, and the pipeline read so nobody is recorded twice. |
| the HR system | read | The company's own employees, who hear of the opening through the internal posting and are never approached as outside candidates. |
| the contact database | read | The people the company already holds, so each person is recorded once. |
| the outside sources the sourcing policy allows | read | Searched for the must-haves alone, with no right to search any other source. |
| the consent record | read | Which past applicants agreed to be kept on file and until when, and who asked never to be approached. |
| the notification channel | write | The request for referrals reaches the teams the plan names, and each draft approach reaches the recruiter. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
