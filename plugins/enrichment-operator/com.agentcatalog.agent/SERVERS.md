# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | write | The empty fields are filled there, each one stamped. |
| the enrichment sources | read | The sources chosen for this fill, and no others. |
| the data dictionary | read | What each empty field means, the values it accepts and the rules it is held to. |
| the consent record | read | Which fields may be filled from outside at all. |
| the review queue | write | Fills under the confidence bar wait there rather than being written. |
| the data warehouse | write | The fill as it ran, by source, with the cost and the rejection rate. |
| the enrichment budget | read | A batch that would exceed it stops at the record it reached. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
