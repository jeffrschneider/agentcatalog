# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the contract repository | read | The executed document at a version, with every exhibit and amendment it names. |
| the signature system | write | The document goes to the named signers in order, and comes back out of there when a deal is lost. |
| the entity list | read | The entity that buys and the one that sells, matched to what the organization holds rather than to the address block on the paper. |
| the approval record | read | Which term off the standard paper is signed for, by whom, against which version. |
| the notification channel | write | The people who act on a booking hear the same booking at the same time. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
