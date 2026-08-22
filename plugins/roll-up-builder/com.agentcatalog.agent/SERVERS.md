# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The open deals in scope as they stand at the cut-off. |
| the pipeline extract store | write | One extract at one moment, kept so any number built from it can be replayed line by line. |
| the rate source | read | One rate table, named and dated, applied once. |
| the category definitions | read | Applied as written, at a version. |
| the hygiene marks | read | A deal the record could not support is counted and flagged rather than dropped. |
| the report store | write | The cuts, the reconciliation and the comparison to the last cycles. |
| the forecast record | write | The frozen version, pinned to its extract, its rate table and its definitions. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
