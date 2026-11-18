# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the signature system | read | The subscription packs as they come back, with who signed, on which page and when. |
| the document store | write | Each subscription as received, the findings on it, and the filed close record. |
| the customer relationship management system, or CRM | read | The commitment each investor stated, which its subscription must match. |
| the screening service | read | Each investor's screening result, which must be clear before its subscription goes to acceptance. |
| the fund accounting system | read | The investor register and the commitments already admitted, which the new close is filed beside. |
| the notification channel | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
