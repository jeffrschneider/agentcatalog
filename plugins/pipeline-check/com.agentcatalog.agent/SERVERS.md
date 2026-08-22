# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | Every open deal as the record holds it at the pull. |
| the CRM | write | The finding written on the deal, and the mark on a deal that still fails. Corrections to amount, close date or stage are not in this grant. |
| the field rules and the stage definitions | read | Read at a version, never from memory. |
| the pricing record | read | The deal amount set against its own line items. |
| the territory map | read | Every open deal carries a live owner in a live territory. |
| the pipeline extract store | read | So a finding can be replayed against the deals it was computed from. |
| the notification channel | write | The deal's owner is told, with the rule and the amount attached. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
