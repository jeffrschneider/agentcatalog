# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the applicant tracking system | write | The chosen candidate, the hiring decision and the outcome, with nothing about what a check found. |
| the background check provider's system | write | Each consented check ordered with only the details it needs, and each error the candidate points to sent back to be corrected. |
| the restricted records store | write | Each result held apart from the hiring record where only the named reviewers can open it, with every opening logged. |
| the consent record | write | The notice of each check and the candidate's signed consent to it. |
| the notification channel | write | The candidate told of a delay, and a request to see the results from anyone outside the named people reaches the head of HR. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
