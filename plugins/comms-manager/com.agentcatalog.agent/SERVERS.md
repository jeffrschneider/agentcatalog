# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the announcement plan and its timeline | write | The date, and what was known at each point. |
| the message record | write | Each audience's wording lands here at a version. |
| the claims register | read |  |
| brand guidelines | read |  |
| the incident record | read | The facts as the people handling the incident establish them. |
| the coverage record | read |  |
| the staged releases | trigger | The pieces go out in the planned order, after the sign-offs. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
