# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the answer library | read | Every answer is read from it at a version, and none is written from memory. |
| the evidence store | read | The reports, certificates and policies the answers point at, each at the version the answer names. |
| the CRM | read | The opportunity the form is attached to and the confidentiality agreement that covers it. |
| the buyer's portal | write | The form filed the way the buyer asked. |
| the document store | write | The response as sent, its date and its receipt. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
