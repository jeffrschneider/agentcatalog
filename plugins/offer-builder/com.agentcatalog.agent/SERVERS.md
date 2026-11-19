# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the applicant tracking system | write | The decision, the reserves, the outcome of the checks, each version of the offer, the signed acceptance and the position marked filled. |
| the HR system | read | The approved position with its level, its pay range and its budget. |
| the compensation records | read | The figure the compensation-analyst agent checked and the limits the agreed terms set. |
| the signature system | trigger | Each draft sent to the named approvers in the order the delegation of authority sets, with no right to sign for any of them. |
| the notification channel | write | The approved letter reaches the candidate the same day the recruiter makes the offer, and an offer near its expiry date reaches the recruiter. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
