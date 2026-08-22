# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the order and contract record | write | Every quote, order and agreed term, with its dates. |
| supplier ordering and booking systems | write | Cap: what it may commit without asking. |
| the exhibitor and venue rules | read | At the version the organizer published. |
| the event plan and its schedule | read |  |
| freight and shipment tracking | read |  |
| the asset store | read | The files the printed and built pieces are made from. |
| the accounting record for the event | read | What has been invoiced and what has been paid. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
