# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the content library | read | The approved sections, each pulled at its current version and recorded at that version. |
| the quoting system | read | The approved quote, its price and the date it stops holding. |
| the claims register | read | What the organization has agreed to say, so nothing is written that cannot be traced to it. |
| the document store | write | One file at one version, dated. |
| the sending system | write | Delivery to the people the decision named, in the format the buyer asked for. |
| the tracking system | read | Who opened it, who it was shared with, and how far they read. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
