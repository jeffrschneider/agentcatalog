# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the asset store | write | Drafts land at versions. |
| brand guidelines | read |  |
| the claims register | read |  |
| the applicant tracking system | read | The approved job, the must-haves and the pay range a job posting is written from. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
