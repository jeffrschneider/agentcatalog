# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the rate card store | read | Every line is priced at a named card version, and the version is recorded beside the price. |
| the entitlement record | read | What the customer already pays for, taken out before a discount is asked for. |
| the cost model | read | The floor the priced deal is set against. |
| the quoting system | write | The priced lines, the term and the date the quote stops being good. |
| the approval record | read | Which exception is signed, by whom, against which version of the quote. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
