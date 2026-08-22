# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the disclosure rules for each market | read | The rules the organization has adopted, at their versions. |
| the claims register | read |  |
| the asset store | read | The material at the version it was submitted at. |
| the distribution plan for the material | read | Which markets and channels it will run in. |
| the approved price and offer terms | read | At the version they were approved at. |
| the agreements behind a paid partnership | read | What the relationship requires to be said. |
| the review record | write | The verdicts land where the signers and the producing agents read them. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
