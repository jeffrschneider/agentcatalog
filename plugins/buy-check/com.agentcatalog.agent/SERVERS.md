# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the media plan | read | At the version the buy was placed against. |
| the rules the buy was placed under | read | At their versions. |
| ad platforms | read | The campaign as configured and what it delivered. |
| the placement and delivery record | read | Where the ads appeared and how often. |
| the exclusion lists in force | read | At their versions. |
| the asset store | read |  |
| the review record | write | The verdicts land where the signers and the buying agent read them. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
