# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the partner record | write | The claim-by-claim finding lands against the candidate. |
| the evidence store | write | Every finding keeps the document, the source and the date it was read. |
| the reference call notes | write | What each customer said, against the questions set beforehand. |
| the contract system | read | The agreements a candidate already holds, where they bear on the gap. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
